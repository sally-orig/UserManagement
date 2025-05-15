from fastapi import FastAPI
from .apis import router

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(router, prefix="/users", tags=["Users"])