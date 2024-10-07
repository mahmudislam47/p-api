from fastapi import FastAPI
from g4f.api import run_api

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, this is your FastAPI app on Vercel!"}

@app.on_event("startup")
async def startup_event():
    run_api()
