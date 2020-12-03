import json
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from accounts.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "chat",
            self.channel_name
        )
        self.accept()
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
        "chat", self.channel_name
        )
        self.close()
        
    def receive(self, text_data):
        # channel_layer = get_channel_layer()
        # if "user" not in self.scope:
        #     print("websocket connect close")
        #     await self.close()
        # else:
        print("hogehoge")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(
            "chat",
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
