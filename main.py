from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> dict:
    return {"status" : "success"}

@app.get("/hola")
def hola() -> str:
    return "Hola!"