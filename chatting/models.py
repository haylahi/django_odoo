from django.db import models

"""

1. The user sends a first message to the chatbot.
2. This opens a scope containing the user’s username, chosen name, and user ID.
3. The application is given a "chat.received_message" event with the event text. It does not have to respond, 
   but could send one, two or more other chat messages back as chat.send_message events if it wanted to.
4. The user sends more messages to the chatbot and more chat.received_message events are generated.
5. After a timeout or when the application process is restarted the scope is closed.

$ python3 manage.py shell
>>> import channels.layers
>>> channel_layer = channels.layers.get_channel_layer()
>>> from asgiref.sync import async_to_sync
>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>> async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}


"""


class ChatMessage(models.Model):
    """
    TODO 1. 聊天室(站内通知，发消息给好友， 聊天组) 2. permission 3. workflow 4. js render table


    """
