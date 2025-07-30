from fastapi import FastAPI

app = FastAPI(title="PDF Summary AI")


@app.get("/")
def get_root():
    return "Hello world"
