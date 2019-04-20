import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index_page(request):
    return render(request, 'chat/index.html')


def room_page(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
