import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AttendanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "attendance_updates",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "attendance_updates",
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            "attendance_updates",
            {
                'type': 'attendance_message',
                'message': message
            }
        )

    async def attendance_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))