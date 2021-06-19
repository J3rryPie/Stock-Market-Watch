import json
from nsetools import Nse
from .models import script
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
channel_layer = get_channel_layer()
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from time import sleep
class NSEConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.user = self.scope["user"]
        print(vars(self.user))
        print(vars(self))
        while (1):
            nse=Nse()
            all = script.objects.values()
            l=[]
            for i in all:
                data = nse.get_quote(i['code'])
                if i['price'] > data['lastPrice']:
                    i.update(state = 'up')
                if i['price'] > data['lastPrice']:
                    i.update(state = 'do')
                if i['price'] > data['lastPrice']:
                    i.update(state = 'un')
                i.update(price = data['lastPrice'])
                i.update(buy_quantity = data['buyQuantity1'])
                i.update(buy_price = data['buyPrice1'])
                i.update(sell_quantity = data['sellQuantity1'])
                i.update(sell_price = data['sellPrice1'])
                i.update(change = data['change'])
                # i.update(change_percentage = round((data['change']*100)/data['lastPrice'],2))
                l.append(data)
            self.send(text_data=json.dumps({'info':l,'status' : 'connected from new sync json consumer'}))
            sleep(60)
        # self.send(text_data=json.dumps({'status' : 'connected from django channels'}))
        
    
    
    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps({'status' : 'we got you'}))


    # def disconnect(self , *args, **kwargs):
    #     print('disconnected')
    
    
    def send_notification(self , event):
        print('send notification')
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload' : data}))
        
        print('send notification')



# class NSEConsumer(AsyncJsonWebsocketConsumer):
    
#     async def connect(self):
#         self.room_name = 'new_consumer'
#         self.room_group_name = "new_consumer_group"
        
#         await(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
        
#         await self.accept()
#         self.user = self.scope["user"]
#         print(self.user)
#         while (1):
#             nse=Nse()
#             all = script.objects.values()
#             for i in all:
#                 data = nse.get_quote(i['code'])
#                 if i['price'] > data['lastPrice']:
#                     i.update(state = 'up')
#                 if i['price'] > data['lastPrice']:
#                     i.update(state = 'do')
#                 if i['price'] > data['lastPrice']:
#                     i.update(state = 'un')
#                 i.update(price = data['lastPrice'])
#                 i.update(buy_quantity = data['buyQuantity1'])
#                 i.update(buy_price = data['buyPrice1'])
#                 i.update(sell_quantity = data['sellQuantity1'])
#                 i.update(sell_price = data['sellPrice1'])
#                 i.update(change = data['change'])
#                 i.update(change_percentage = round((data['change']*100)/data['lastPrice'],2))
#             await self.send(text_data=json.dumps({'info':data,'status' : 'connected from new async json consumer'}))
        
        
#     async def receive(self, text_data):
#         print(text_data)
#         await self.send(text_data=json.dumps({'status' : 'we got you'}))


#     async def disconnect(self , *args, **kwargs):
#         await print('disconnected')
    
#     async  def send_notification(self , event):
#         data = json.loads(event.get('value'))
#         await self.send(text_data=json.dumps({'payload' : data}))