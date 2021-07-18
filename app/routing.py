from django.urls import re_path

from app import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<user_name>\w+)/$', consumers.Consumer.as_asgi()),
]