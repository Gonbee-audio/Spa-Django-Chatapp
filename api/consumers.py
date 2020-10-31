from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from accounts.models import User
from channels.layers import get_channel_layer


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        """
        self.user = await database_sync_to_async(self.get_name)()
        # 認証チェック
        if not self.scope['user'].is_authenticated:
            self.close()
            return

        self.mine = self.scope['user']

        async_to_sync(self.channel_layer.add)(
            self.mine
        )
        # 接続を受け入れる
        """
        self.accept()

    """
    def get_name(self):
        return User.objects.all().username
    """
    
    def disconnect(self, close_code):
        self.close()
        
    async def receive(self, text_data=None, bytes_data=None):
        # channel_layer = get_channel_layer()
        # if "user" not in self.scope:
        #     print("websocket connect close")
        #     await self.close()
        # else:
                self.send(
                message=text_data,
            )
