# author: Liberty
# date: 2019/4/30 11:08

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from chatting import routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
})
