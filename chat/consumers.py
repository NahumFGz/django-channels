import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Message
from .serializers import MessageSerializer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "chat_room"
        self.room_group_name = f"chat_{self.room_name}"

        # Unirse al grupo
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Salir del grupo
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Manejar mensajes desde WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        username = data["username"]
        content = data["content"]

        # Guardar mensaje en la base de datos
        message = Message.objects.create(username=username, content=content)

        # Serializar mensaje
        serializer = MessageSerializer(message)

        # Enviar mensaje al grupo
        await self.channel_layer.group_send(self.room_group_name, {"type": "chat_message", "message": serializer.data})

    # Manejar mensajes desde el grupo
    async def chat_message(self, event):
        message = event["message"]

        # Enviar mensaje al WebSocket
        await self.send(text_data=json.dumps(message))
