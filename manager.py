# 🔗 WebSocket 连接管理器 —— 负责记住所有在线客户端、广播消息

from fastapi.websockets import WebSocket


class ConnectionManager:
    """🧑‍🤝‍🧑 管理所有 WebSocket 连接 + 当前共享状态的类"""

    def __init__(self):
        # 📋 当前所有在线的 WebSocket 连接列表
        self.active_connections: list[WebSocket] = []
        # 📝 服务器当前保存的文本内容（新客户端连上时会推送给他）
        self.current_text = ""
        # 🖼️ 服务器当前保存的图片（base64 data URL 格式，空字符串表示没有图片）
        self.current_image = ""

    async def connect(self, ws: WebSocket):
        """🟢 接受一个新的 WebSocket 连接并加入列表"""
        await ws.accept()  # 必须调用 accept() 才算建立成功
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        """🔴 客户端断开，从列表中移除"""
        self.active_connections.remove(ws)

    async def broadcast(self, message: str, sender: WebSocket):
        """📢 把消息广播给除发送者以外的所有人

        Args:
            message:  JSON 字符串（前端用 JSON.parse 解析）
            sender:   发送者本人（不给自己发，避免回显）
        """
        for connection in self.active_connections:
            if connection != sender:
                try:
                    await connection.send_text(message)  # 📤 推给其他人
                except Exception:
                    pass  # ⚠️ 忽略发送失败（比如对方已经断开但还没从列表移除）


# 🏭 模块级单例 —— 整个应用只用一个 ConnectionManager 实例
# 这样 routes.py 和 app.py（如果需要）import 的都是同一个对象
manager = ConnectionManager()
