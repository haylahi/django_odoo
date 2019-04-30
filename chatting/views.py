import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'chat/index.html', {
        'frontUrl': '/chat/'
    })


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'roomName': mark_safe(room_name),
    })
