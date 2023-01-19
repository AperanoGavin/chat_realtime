from django.urls import path , include
from chat.consumers import ChatConsumer

# Ici, "" est routé vers l'URL ChatConsumer qui
# gérera la fonctionnalité de chat.
websocket_urlpatterns = [
	path("" , ChatConsumer.as_asgi()) ,
]
