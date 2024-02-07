# Channels ve ASGI gelen bağlantıyı iki bileşene ayırır - kapsam, olaylar
# scope- (django'nun request'ine benzer), bir web isteğinin yapıldığı yol, bir web 
#soketinin Ip adresi, kullanıcı gibi tek bir gelen bağlantı hakkında bir dizi ayrıntıdır
# events - bağlanma, bağlantıyı kesme, mesaj alma olayı

import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        msg = data['message']
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_messages',
                'messages': msg,
                'user': str(self.scope['user'])
            }
        )

    async def chat_messages(self, event):
        msg = event["messages"]
        user = event["user"]
        await self.send(text_data=json.dumps({"message": msg, "user": user}))

    async def game_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))


class Chating(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,self.channel_name
        )
        self.accept()
    
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,self.channel_name
        )
    
    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        msg = data["message"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                "type":"chat_messages",
                "messages":msg ,
                "user": str(self.scope['user'])
            }
        )
    def chat_messages(self,event):
        msg = event["messages"]
        self.send(text_data=json.dumps({"message": msg,"user":event["user"]}))