"""Module principal de l'application FastAPI pour le TP3 DevOps."""

import socket
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="TP2 FastAPI App")


@app.get("/")
def read_root():
    """Point d'entree racine de l'API."""
    return {"message": "it works !"}


def get_ip_address() -> str:
    """Recupere l'adresse IP locale de la machine."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        ip_addr = sock.getsockname()[0]
    except OSError:
        ip_addr = "127.0.0.1"
    finally:
        sock.close()
    return ip_addr


@app.get("/greeting")
def greeting(name: str):
    """Salue l'utilisateur et renvoie les informations reseau."""
    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": socket.gethostname(),
        "IP": get_ip_address()
    }


@app.get("/addition")
def addition(a: int, b: int):
    """Additionne deux entiers."""
    return {
        "result a+b": a + b,
        "developer": "Dev1"
    }


@app.get("/soustraction")
def soustraction(a: int, b: int):
    """Calcule la difference entre deux entiers."""
    return {
        "result": a - b,
        "developer": "Dev1"
    }


class OperationInput(BaseModel):
    """Modele de donnees pour les operations a deux operandes."""
    a: float
    b: float


@app.post("/multiply")
def multiply(data: OperationInput):
    """Multiplie deux nombres reels."""
    return {
        "result": data.a * data.b,
        "developer": "Dev1"
    }


@app.post("/divide")
def divide(data: OperationInput):
    """Divise le premier nombre par le second avec verification de division par zero."""
    if data.b == 0:
        raise HTTPException(
            status_code=400,
            detail="Erreur: Division par zero impossible."
        )
    return {
        "result": data.a / data.b,
        "developer": "Dev2"
    }


items_db = {
    1: "Serveur",
    2: "Base de donnees",
    3: "Routeur"
}


@app.delete("/remove/{item_id}")
def remove_item(item_id: int):
    """Supprime un element de la base de donnees par son identifiant."""
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="Element non trouve"
        )

    deleted = items_db.pop(item_id)
    return {
        "message": f"Element {item_id} ({deleted}) supprime",
        "developer": "Dev1"
    }
