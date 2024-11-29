from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [path(r"ws/open_chat/<uuid>/", consumers.JoinAndLeave.as_asgi())]