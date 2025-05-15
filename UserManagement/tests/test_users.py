import pytest
from httpx import AsyncClient, ASGITransport
from ..models import User
from .test_db import setup_test_db, teardown_test_db, TestingSessionLocal, app, override_get_db
from datetime import date
from unittest.mock import MagicMock
from fastapi import Depends

transport = ASGITransport(app=app)

@pytest.fixture(scope="module", autouse=True)
def prepare_database():
    setup_test_db()

    db = TestingSessionLocal()
    db.add_all([
        User(email="test1@mail.com", age=15, date_of_birth=date(1998, 1, 1)),
        User(email="test2@mail.com", age=25, date_of_birth=date(2008, 1, 1)),
        User(email="test3@hotmail.com", age=35, date_of_birth=date(1998, 1, 1)),
    ])
    db.commit()
    db.close()

    yield
    teardown_test_db()


# Test cases for get all users
@pytest.mark.asyncio
async def test_get_all_users():
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(response.json()) == 3

# @pytest.mark.asyncio
# async def test_get_all_users_empty_db():
#     async with AsyncClient(transport=transport, base_url="http://test") as client:
#         response = [await client.get("/users")]
#     assert response.status_code == 404
#     assert response.json() == {"detail": "No users found"}
    

# Test cases for get user by ID
@pytest.mark.asyncio
async def test_get_user_by_id():
    TEST_ID = 2
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get(f"/users/{TEST_ID}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == TEST_ID
    assert data["email"] == "test2@mail.com"
    assert data["age"] == 25
    assert data["date_of_birth"] == "2008-01-01"

@pytest.mark.asyncio
async def test_get_user_not_found():
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get(f"/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

@pytest.mark.asyncio
async def test_get_user_invalid_id():
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/users/invalid_id")
    assert response.status_code == 422