from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import socket

app = FastAPI(title="TP2 FastAPI App")


@app.get("/")
def read_root():
    return {"message": "it works !"}


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


@app.get("/greeting")
def greeting(name: str):
    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": socket.gethostname(),
        "IP": get_ip_address()
    }


@app.get("/addition")
def addition(a: int, b: int):
    return {
        "result a+b": a + b,
        "developer": "Dev1"
    }

class OperationInput(BaseModel):
    a: float
    b: float



@app.post("/divide")
def divide(data: OperationInput):
    if data.b == 0:
        raise HTTPException(
            status_code=400,
            detail="Erreur: Division par zero impossible."
        )
    return {"result": data.a / data.b, "developer": "Dev2"}

@app.post("/multiply")
def multiply(data: OperationInput):
    return {
        "result": data.a * data.b,
        "developer": "Dev1"
    }

items_db = {
    1: "Serveur",
    2: "Base de donnees",
    3: "Routeur"
}
@app.delete("/remove/{id}")
def remove_item(id: int):
    if id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="Element non trouve"
        )

    deleted = items_db.pop(id)

    return {
        "message": f"Element {id} ({deleted}) supprime",
        "developer": "Dev1"
    }