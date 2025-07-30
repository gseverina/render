from fastapi import FastAPI
from routes import router  # 👈 import your router

app = FastAPI()

app.include_router(router, prefix="/api")

