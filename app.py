import socket
import urllib.request
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocket, WebSocketDisconnect


def get_local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def get_public_ip() -> str:
    try:
        req = urllib.request.Request(
            "https://api.ipify.org", headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.read().decode().strip()
    except Exception:
        return "获取失败"


local_ip = get_local_ip()
public_ip = get_public_ip()

port = 60628

print(f"\n  局域网: http://{local_ip}:{port}")
if public_ip != "获取失败":
    print(f"  公网:   http://{public_ip}:{port}")
print(f"  本机:   http://127.0.0.1:{port}\n")

app = FastAPI()

HERE = Path(__file__).parent
app.mount("/assets", StaticFiles(directory=str(HERE / "assets")), name="assets")
template = (HERE / "templates" / "index.html").read_text(encoding="utf-8")

current_text = ""


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        self.active_connections.remove(ws)

    async def broadcast(self, message: str, sender: WebSocket):
        for connection in self.active_connections:
            if connection != sender:
                try:
                    await connection.send_text(message)
                except Exception:
                    pass


manager = ConnectionManager()


@app.get("/", response_class=HTMLResponse)
async def get_index():
    return template.replace("__INITIAL_TEXT__", current_text, 1)


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    global current_text
    await manager.connect(ws)
    try:
        while True:
            data = await ws.receive_text()
            current_text = data
            await manager.broadcast(data, sender=ws)
    except WebSocketDisconnect:
        manager.disconnect(ws)
