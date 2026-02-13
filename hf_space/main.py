from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "token": os.environ.get("GA2_TOKEN_142A", "Not Found")}

@app.get("/health")
def health():
    return {"status": "ok"}
