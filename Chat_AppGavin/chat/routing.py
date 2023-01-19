from django.urls import path , include
from . import consumer

# Ici, "" est routé vers l'URL ChatConsumer qui
# gérera la fonctionnalité de chat.
websocket_urlpatterns = [
	path('chat/' , consumer.ChatConsumer.as_asgi()) ,
]
