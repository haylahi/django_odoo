# author: Liberty
# date: 2019/4/30 12:06
import json
from datetime import datetime

from channels.consumer import SyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

from base.utils import FORMAT_DATETIME


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{name}'.format(name=self.room_name)

        # join a room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        _message = text_data_json.get('message')
        _now = datetime.now().strftime(FORMAT_DATETIME)

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': '{}-->{}'.format(_message, _now)
            }
        )

    async def chat_message(self, event):
        _msg = event.get('message')

        # 发送到 WebSocket
        await self.send(text_data=json.dumps({'message': _msg}))


class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        self.send({"type": "websocket.send", "text": event["text"]})
