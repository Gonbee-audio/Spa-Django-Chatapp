import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from accounts.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


from .models import ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        

        await self.channel_layer.group_add(
            "chat",
            self.channel_name,
        )
        await self.accept()




    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
        "chat", self.channel_name
        )
        await self.close()
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send_message(message)

        await self.channel_layer.group_send(
            "chat",
            {
                'type': 'chat_message',
                'message': message,
                'id': self.p_id,
            }
        )

    @database_sync_to_async
    def send_message(self, message):
        print(message)
        mes = ChatMessage.objects.create(
            username=message["username"],
            nickname=message["username"],
            text=message["text"],
            icon="text.png" ,
        )
        self.p_id = mes.id
        return self.p_id


    async def chat_message(self, event):
        m_id = event['id']
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
            'id': m_id
        }))
    
