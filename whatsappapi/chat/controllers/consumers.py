import json
from channels.generic.websocket import AsyncWebsocketConsumer
from ..services.tasks import enter_chatroom, leave_chatroom


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

        # Trigger Celery task to enter user to 
        enter_chatroom.delay(self.user.id, self.room_name)

    async def disconnect(self, close_code):
        leave_chatroom.delay(self.user.id, self.room_name)

        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Logic to handle received message
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
