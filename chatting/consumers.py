# author: Liberty
# date: 2019/4/30 12:06
import json
from datetime import datetime

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from base.utils import FORMAT_DATETIME


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{n}'.format(n=self.room_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        _message = text_data_json.get('message')
        _now = datetime.now().strftime(FORMAT_DATETIME)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'chat_message',
                'message': '{}{}'.format(_message, _now)
            }
        )

    def chat_message(self, event):
        _msg = event.get('message')

        # 发送到WebSocket
        self.send(text_data=json.dumps({'message': _msg}))
