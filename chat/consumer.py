# Channels ve ASGI gelen bağlantıyı iki bileşene ayırır - kapsam, olaylar
# scope- (django'nun request'ine benzer), bir web isteğinin yapıldığı yol, bir web 
#soketinin Ip adresi, kullanıcı gibi tek bir gelen bağlantı hakkında bir dizi ayrıntıdır
# events - bağlanma, bağlantıyı kesme, mesaj alma olayı

import json
# from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the room name from the URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # Join the room group
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']
        # Handle different message types
        if message_type == 'paddlePosition':
            # Update the paddle position
            self.paddle_position = data['position']

            # Send the updated paddle position to other users in the room
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'paddlePosition',
                    'player': self.channel_name,
                    'position': self.paddle_position
                }
            )

        elif message_type == 'ballPosition':
            # Update the ball position
            self.ball_position = data['position']
            # Send the updated ball position to other users in the room
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'ballPosition',
                    'position': self.ball_position
                }
            )

        elif message_type == 'playerScore':
            # Update the player score
            self.player_score = data['score']
            print(data['score'])
            # Send the updated player score to other users in the room
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'playerScore',
                    'player': self.channel_name,
                    'score': self.player_score
                }
            )

        elif message_type == 'gameOver':
            # The game is over
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'gameOver'
                }
            )

    # Send message to WebSocket
    async def send_message(self, data):
        await self.send(json.dumps(data))

    # Handle paddle position updates from other users
    async def paddlePosition(self, event):
        player = event['player']
        position = event['position']

        # Update the paddle position
        if player != self.channel_name:
            self.paddle_position = position

        # Send the updated paddle position to the client
        await self.send_message({
            'type': 'paddlePosition',
            'player': player,
            'position': position
        })

    # Handle ball position updates from other users
    async def ballPosition(self, event):
        position = event['position']

        # Update the ball position
        self.ball_position = position

        # Send the updated ball position to the client
        await self.send_message({
            'type': 'ballPosition',
            'position': position
        })

    # Handle player score updates from other users
    async def playerScore(self, event):
        player = event['player']
        score = event['score']

        # Update the player score
        if player != self.channel_name:
            self.player_score = score

        # Send the updated player score to the client
        await self.send_message({
            'type': 'playerScore',
            'player': player,
            'score': score
        })

    # Handle game over messages from other users
    async def gameOver(self, event):
        # Send the game over message to the client
        await self.send_message({
            'type': 'gameOver'
        })