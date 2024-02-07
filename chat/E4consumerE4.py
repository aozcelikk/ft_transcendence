# Channels ve ASGI gelen bağlantıyı iki bileşene ayırır - kapsam, olaylar
# scope- (django'nun request'ine benzer), bir web isteğinin yapıldığı yol, bir web 
#soketinin Ip adresi, kullanıcı gibi tek bir gelen bağlantı hakkında bir dizi ayrıntıdır
# events - bağlanma, bağlantıyı kesme, mesaj alma olayı

import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

import asyncio

from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message

class GameConsumer(AsyncConsumer):
    room = None

    async def websocket_connect(self, event):
        """
        Called when the websocket connection is established.
        """
        print("Websocket connected.")

        # Get the room name from the path
        room_name = self.scope['url_route']['kwargs']['room_name']

        # Get the room object from the database
        self.room = await database_sync_to_async(Room.objects.get)(room_name=room_name)

        # Add the consumer to the room's group
        await self.channel_layer.group_add(
            self.room.group_name,
            self.channel_name
        )

        # Accept the websocket connection
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        """
        Called when a message is received from the websocket.
        """
        print("Websocket message received.")

        # Get the data from the message
        data = event['text']

        # Parse the data as JSON
        data = json.loads(data)

        # Get the message type
        message_type = data['type']

        # Handle the message based on the type
        if message_type == 'paddlePosition':
            # Get the player number and paddle position from the data
            player_number = data['player']
            paddle_position = data['position']

            # Update the paddle position in the database
            if player_number == 1:
                self.room.player1_paddle_position = paddle_position
            else:
                self.room.player2_paddle_position = paddle_position

            await database_sync_to_async(self.room.save)()

            # Send the paddle position to the other player
            await self.channel_layer.group_send(
                self.room.group_name,
                {
                    'type': 'paddlePosition',
                    'player': player_number,
                    'position': paddle_position
                }
            )

        elif message_type == 'ballPosition':
            # Get the ball position from the data
            ball_position = data['position']

            # Update the ball position in the database
            self.room.ball_position = ball_position
            await database_sync_to_async(self.room.save)()

            # Send the ball position to both players
            await self.channel_layer.group_send(
                self.room.group_name,
                {
                    'type': 'ballPosition',
                    'position': ball_position
                }
            )

        elif message_type == 'playerScore':
            # Get the player number and score from the data
            player_number = data['player']
            score = data['score']

            # Update the player's score in the database
            if player_number == 1:
                self.room.player1_score = score
            else:
                self.room.player2_score = score

            await database_sync_to_async(self.room.save)()

            # Send the player's score to both players
            await self.channel_layer.group_send(
                self.room.group_name,
                {
                    'type': 'playerScore',
                    'player': player_number,
                    'score': score
                }
            )

        elif message_type == 'gameOver':
            # Send the game over message to both players
            await self.channel_layer.group_send(
                self.room.group_name,
                {
                    'type': 'gameOver'
                }
            )

    async def websocket_disconnect(self, event):
        """
        Called when the websocket connection is closed.
        """
        print("Websocket disconnected.")

        # Remove the consumer from the room's group
        await self.channel_layer.group_discard(
            self.room.group_name,
            self.channel_name
        )

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