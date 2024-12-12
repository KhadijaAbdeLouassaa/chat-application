import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from chats.models import ChatRoom
from friends.models import Friend
from django.contrib.auth.models import User
class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.receiver = self.scope['url_route']['kwargs']['username']
        self.user = self.scope['user'].username
        
        self.room_group_name = f"chat_{'_'.join(sorted([self.user, self.receiver]))}"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        load_data = json.loads(text_data)
        sender = load_data['sender']
        receiver = load_data['receiver']
        message = load_data['message']
        time = load_data['time']
        await self.save_message(message, time, sender,receiver)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'messages',
                'message': message,
                'time': time,
                'sender': sender
            }
        )
        
    async def messages(self, event):
        message = event['message']
        time = event['time']
        sender = event['sender']
        
        await self.send(text_data=json.dumps({
            'message': message,
            'time': time,
            'sender': sender
        }))
    @sync_to_async
    def save_message(self,message,time, sender,receiver):
      
        save_chat = ChatRoom.objects.create(
                        message = message,
                        sender =  User.objects.get(username = sender),
                        receiver = User.objects.get(username=receiver ),
                        timestamp = time)
        save_chat.save()
        