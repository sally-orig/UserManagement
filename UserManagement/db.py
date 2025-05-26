from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# DATABASE_URL = f"mysql+mysqldb://admin:admintest@ld77.ci9mca82oykl.us-east-1.rds.amazonaws.com:3306/ld-dev"
DATABASE_URL = os.getenv("DB_URL", "mysql+mysqldb://admin:admin123@mysql:3306/usermanagement")
print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
Base = declarative_base(metadata=metadata)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()