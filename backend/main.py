from fastapi import FastAPI
from routes.process import router

app = FastAPI()
app.include_router(router)