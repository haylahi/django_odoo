# author: Liberty
# date: 2019/4/30 12:06

from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    """
    web socket 协议

    """

    def connect(self):
        print('recv a conn')
        self.accept()

    def disconnect(self, code):
        print('a coon leave : ', code)

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        print('recv data is ', text_data_json)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
