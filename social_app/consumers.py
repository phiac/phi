# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio

class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Handle incoming video frames
        pass
