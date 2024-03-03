# Channels ve ASGI gelen bağlantıyı iki bileşene ayırır - kapsam, olaylar
# scope- (django'nun request'ine benzer), bir web isteğinin yapıldığı yol, bir web 
#soketinin Ip adresi, kullanıcı gibi tek bir gelen bağlantı hakkında bir dizi ayrıntıdır
# events - bağlanma, bağlantıyı kesme, mesaj alma olayı

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from .models import Room
from channels.db import database_sync_to_async
import asyncio
import json


class GameConsumer(AsyncWebsocketConsumer):
    is_active = True  # Oyuncunun sekmede olup olmadığını belirleyen özellik
    async def connect(self):
        self.player_id = self.scope['url_route']['kwargs']['room_name']
        self.room_name = 'player_%s' % self.player_id
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )

        await self.accept()

    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name,
        )
        

    # Websocket mesaj kontrol
    async def receive(self, text_data):
        if text_data:
            print("Received message:", text_data)
            try:
                data = json.loads(text_data)
                print("Parsed JSON data:", data['type'])
                if data['type']:
                    await self.send(text_data=json.dumps({"text": data['type']}))
            except json.JSONDecodeError as e:
                print("Error: Invalid JSON format -", str(e))
            data = json.loads(text_data)
            message_type = data['type']

            if message_type == 'update':
                self.player = data['player']
                
                await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'update',
                    'player': self.player
                }
                )

            elif message_type == 'paddlePosition':
                self.paddle_position = data['position']
                self.player = data['player']

                await self.channel_layer.group_send(
                    self.room_name,
                    {
                        'type': 'paddlePosition',
                        'player': self.player,
                        'position': self.paddle_position
                    }
                )

            elif message_type == 'ballPosition':
                self.ball_position = data['position']
                await self.channel_layer.group_send(
                    self.room_name,
                    {
                        'type': 'ballPosition',
                        'position': self.ball_position
                    }
                )

            elif message_type == 'playerScore':
                self.player_score = data['score']
                self.player = data['player']
                await self.channel_layer.group_send(
                    self.room_name,
                    {
                        'type': 'playerScore',
                        'player': self.player,
                        'score': self.player_score
                    }
                )

            elif message_type == 'colorAll':
                self.player_color = data['color']
                self.player = data['player']
                await self.channel_layer.group_send(
                    self.room_name,
                    {
                        'type': 'colorAll',
                        'player': self.player,
                        'color': self.player_color
                    }
                )

            elif message_type == 'gameOver':
                await self.channel_layer.group_send(
                    self.room_name,
                    {
                        'type': 'gameOver',
                    }
                )
        else:
            print("Error: Empty message received")

    async def send_message(self, data):
        if data:
            if self.is_active:
                try:
                    await self.send(json.dumps(data))
                except Exception as e:
                    print()


    async def update(self, event):
        player = event['player']
        await self.send_message({
            'type': 'update',
            'player': player
        })

    async def paddlePosition(self, event):
        player = event['player']
        position = event['position']

        if player != self.channel_name:
            self.paddle_position = position

        await asyncio.sleep(0.01)
        await self.send_message({
            'type': 'paddlePosition',
            'player': player,
            'position': position
        })


    async def ballPosition(self, event):
        if self.is_active:
            position = event['position']
            self.ball_position = position
            await asyncio.sleep(0.01)
            await self.send_message({
                'type': 'ballPosition',
                'position': position
            })


    async def playerScore(self, event):
        player = event['player']
        score = event['score']

        if player != self.channel_name:
            self.player_score = score

        await self.send_message({
            'type': 'playerScore',
            'player': player,
            'score': score
        })

    async def colorAll(self, event):
        player = event['player']
        color = event['color']

        if player != self.channel_name:
            self.player_color = color

        await self.send_message({
            'type': 'colorAll',
            'player': player,
            'color': color
        })
    

    async def gameOver(self, event):
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



class SohbetAnasayfaConsumer(AsyncWebsocketConsumer):
    kisi = 0

    async def connect(self):
        SohbetAnasayfaConsumer.kisi += 1
        self.room_name = 'sohbet_anasayfa'
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Odadan ayrıl
        SohbetAnasayfaConsumer.kisi -= 1
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']

        if message_type == 'update':
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'update',
                    'giris': data['giris'],
                    'sayfa': data['sayfa'],
                    'yenile': data['yenile'],
                }
            )

    async def update(self, event):
        event['giris'] = SohbetAnasayfaConsumer.kisi
        # Mesajı tüm oda üyelerine gönder
        await self.send_message({
                'type': 'update',
                'giris': event['giris'],
                'sayfa': 'yenile',
                'yenile': event['yenile'],
            })

    async def send_message(self, data):
        if data:
            try:
                await self.send(json.dumps(data))
            except Exception as e:
                print()




# class SohbetAnasayfaConsumer(AsyncWebsocketConsumer):
#     kisi = 0

#     async def connect(self):
#         SohbetAnasayfaConsumer.kisi += 1
#         self.room_name = 'sohbet_anasayfa'
#         await self.channel_layer.group_add(
#             self.room_name,
#             self.channel_name
#         )

#         # Kullanıcı bağlandığında tüm sayfaları yenile
#         # await self.channel_layer.group_send(
#         #     self.room_name,
#         #     {
#         #         'type': 'update',
#         #         'giris': 1,
#         #         'sayfa': 'geldi',
#         #         'yenile': 'yenile',
#         #     }
#         # )

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Odadan ayrıl
#         SohbetAnasayfaConsumer.kisi -= 1
#         await self.channel_layer.group_discard(
#             self.room_name,
#             self.channel_name
#         )

#         # Kullanıcı çıktığında tüm sayfaları yenile
#         # await self.channel_layer.group_send(
#         #     self.room_name,
#         #     {
#         #         'type': 'update',
#         #         'giris': -1,
#         #         'sayfa': 'gitti',
#         #         'yenile': 'yenile',
#         #     }
#         # )

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message_type = data['type']

#         if message_type == 'update':
#             await self.channel_layer.group_send(
#                 self.room_name,
#                 {
#                     'type': 'update',
#                     'giris': data['giris'],
#                     'sayfa': data['sayfa'],
#                     'yenile': data['yenile'],
#                 }
#             )

#     async def update(self, event):
#         giris = event['giris']
#         # Mesajı tüm oda üyelerine gönder
#         print(event['yenile'])
#         await self.send_message({
#                 'type': 'update',
#                 'giris': SohbetAnasayfaConsumer.kisi,
#                 'sayfa': 'yenile',
#                 'yenile': event['yenile'],
#             })

#     async def send_message(self, data):
#         if data:
#             try:
#                 await self.send(json.dumps(data))
#             except Exception as e:
#                 print()

