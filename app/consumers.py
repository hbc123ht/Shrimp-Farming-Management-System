from channels.generic.websocket import AsyncWebsocketConsumer
import json


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_name = self.scope['url_route']['kwargs']['user_name']

        await self.channel_layer.group_add(
            self.user_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.user_name,
            self.channel_name
        )
        await self.close()
    
    async def update_params(self, event):
        await self.send(text_data=json.dumps(event['text']))

