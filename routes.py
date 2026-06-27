# 🛣️ 路由模块 —— 定义 HTTP 页面接口 和 WebSocket 实时同步接口

import json  # 🧩 用来把 Python dict 转成 JSON 字符串发给前端

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.websockets import WebSocket, WebSocketDisconnect

from network import HERE
from manager import manager

# 📍 APIRouter 代替 app.get / app.websocket，方便拆分到单独的文件
router = APIRouter()

# 📄 启动时一次性把 index.html 读入内存，避免每次请求都读磁盘
template = (HERE / "templates" / "index.html").read_text(encoding="utf-8")


@router.get("/", response_class=HTMLResponse)
async def get_index():
    html = template.replace("__INITIAL_TEXT__", manager.current_text, 1)
    return html


@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    """🔌 WebSocket 实时同步端点

    通信协议（JSON）：
      { "type": "text",  "data": "..." }       ← 文本内容更新
      { "type": "image", "data": "data:..." }   ← 图片内容更新
      { "type": "clear", "target": "text" }      ← 清空文本
      { "type": "clear", "target": "image" }     ← 清空图片
    """
    await manager.connect(ws)

    try:
        # ✨ 新客户端连上后，先把当前状态推给他
        await ws.send_text(json.dumps({"type": "text", "data": manager.current_text}))
        if manager.current_image:
            await ws.send_text(
                json.dumps({"type": "image", "data": manager.current_image})
            )

        # 🔄 持续接收客户端的消息并广播给其他人
        while True:
            data = await ws.receive_text()  # 收到一条消息（JSON 字符串）
            msg = json.loads(data)  # 解析成 Python dict
            msg_type = msg.get("type")

            if msg_type == "text":
                # 📝 更新服务器上的文本状态
                manager.current_text = msg.get("data", "")
            elif msg_type == "image":
                # 🖼️ 更新服务器上的图片状态
                manager.current_image = msg.get("data", "")
            elif msg_type == "clear":
                # 🗑️ 清空指定的内容
                target = msg.get("target", "")
                if target == "text":
                    manager.current_text = ""
                elif target == "image":
                    manager.current_image = ""

            # 📢 把消息广播给其他在线客户端
            await manager.broadcast(data, sender=ws)

    except WebSocketDisconnect:
        # 👋 客户端断开连接
        manager.disconnect(ws)
