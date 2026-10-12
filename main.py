from fastapi import FastAPI

app = FastAPI(title="TP2 FastAPI App")


@app.get("/")
def read_root():
    return {"message": "it works !"}
