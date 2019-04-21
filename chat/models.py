# author: Liberty
# date: 2019/4/21 23:29

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models

from base.models import UserProfile


class MessageModel(models.Model):
    """message"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='User', related_name='from_user')
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Recipient', related_name='to_user')
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True, editable=False)
    body = models.TextField('Content')

    def __str__(self):
        return self.id

    def characters(self):
        return len(self.body)

    def notify_ws_clients(self):
        notification = {
            'type': 'recieve_group_message',
            'message': '{}'.format(self.id)
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
        async_to_sync(channel_layer.group_send)("{}".format(self.recipient.id), notification)

    def save(self, *args, **kwargs):
        """
            Trims white spaces, saves the message and notifies the recipient via WS
            if the message is new.
        """
        new = self.id
        self.body = self.body.strip()
        super().save(*args, **kwargs)
        if new is None:
            self.notify_ws_clients()

    class Meta:
        db_table = 'chat_message'
        ordering = ['-timestamp']
