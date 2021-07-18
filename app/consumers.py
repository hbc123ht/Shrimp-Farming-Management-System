from channels.generic.websocket import AsyncWebsocketConsumer
import json


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
       
        await self.accept()

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, text_data=None,bytes_data = None):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'recieve_group_message',
                'message': message
            }
        )

    async def recieve_group_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(
             text_data=json.dumps({
            'message': message
        }))