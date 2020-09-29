from channels.generic.websocket import JsonWebsocketConsumer


class ChatConsumer(JsonWebsocketConsumer):

    def connect(self):
        # 認証チェック
        if not self.scope['users'].is_authenticated:
            self.close()
            return

        self.user = self.scope['users']
        # 接続を受け入れる
        self.accept()