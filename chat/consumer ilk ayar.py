# Channels ve ASGI gelen bağlantıyı iki bileşene ayırır - kapsam, olaylar
# scope- (django'nun request'ine benzer), bir web isteğinin yapıldığı yol, bir web 
#soketinin Ip adresi, kullanıcı gibi tek bir gelen bağlantı hakkında bir dizi ayrıntıdır
# events - bağlanma, bağlantıyı kesme, mesaj alma olayı

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room


class GameConsumer(AsyncWebsocketConsumer):
    is_active = True  # Oyuncunun sekmede olup olmadığını belirleyen özellik
    async def connect(self):
        # Get the room name from the URL
        self.player_id = self.scope['url_route']['kwargs']['room_name']
        self.room_name = 'player_%s' % self.player_id
        # Join the room group
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name,
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']
        # Handle different message types
        if message_type == 'paddlePosition':
            # Update the paddle position
            self.paddle_position = data['position']
            self.player = data['player']

            # Send the updated paddle position to other users in the room
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'paddlePosition',
                    'player': self.player,
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
            self.player = data['player']
            # Send the updated player score to other users in the room
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'playerScore',
                    'player': self.player,
                    'score': self.player_score
                }
            )

        elif message_type == 'gameOver':
            # The game is over
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'gameOver',
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
        if self.is_active:
            position = event['position']

            # Update the ball position
            self.ball_position = position

            # await self.channel_layer.group_send(self.player_id, {
            #         'type': 'ballPosition',
            #         'position': position
            # })

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
            'type': 'gameOver',
        })

        await self.save_game_over_status()

    async def save_game_over_status(self):
        room = await self.get_room(self)
        room.is_over = True
        await self.save_room(room)

    @staticmethod
    @sync_to_async
    def get_room(self):
        return Room.objects.get(room_name=self.player_id)

    @staticmethod
    @sync_to_async
    def save_room(room):
        room.save()

