from fastapi import FastAPI

app = FastAPI(title="Corpus Dev Container FastAPI")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}
