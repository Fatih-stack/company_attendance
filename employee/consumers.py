import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AttendanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Katılım grubuna katılma
        self.group_name = 'attendance_updates'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Katılım grubundan ayrılma
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # İstemciden mesaj alındığında
        data = json.loads(text_data)
        message = data.get('message', '')

        # Gruba mesaj gönder
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'attendance_message',
                'message': message
            }
        )

    async def attendance_message(self, event):
        # Gruba mesaj gönderildiğinde istemciye mesaj iletme
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))