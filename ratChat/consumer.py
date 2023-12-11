import json
from mailbox import Message
import base64

from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import RatRoom, RatMessages
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket conectado")

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        print("WebSocket SE DESCONECTO ---")

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    #Envio de imagenes
    async def send_image(self, image_path):
        with open(image_path, 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        await self.send(text_data=json.dumps({
            'type': 'image',
            'image_data': image_data,
        }))
        
    #Recibo de mensajes, e imagenes
    async def receive(self, text_data):
        data = json.loads(text_data)

        message = data['message']
        room = data['room']
        username = data['username']

        """ if data['type'] == 'imagen':
            imagen_id = data['imagen_id']
 """
        await self.save_message(username, room, message)

        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'room':room
                }
            )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data = json.dumps({
            'message' : message,
            'username' : username,
            'room':room
                                
        }))
    
    @sync_to_async
    def save_message(self, username, room , message):
        user = User.objects.get(username = username)
        room = RatRoom.objects.get(slug=room)

        RatMessages.objects.create(user=user, room=room, content=message)