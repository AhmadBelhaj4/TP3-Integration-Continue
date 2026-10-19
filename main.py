from fastapi import FastAPI
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
from pydantic import BaseModel

class OperationInput(BaseModel):
    a: float
    b: float

@app.post("/multiply")
def multiply(data: OperationInput):
    return {
        "result": data.a * data.b,
        "developer": "Dev1"
    }