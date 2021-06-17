import json
from nsetools import Nse
from .models import script
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
channel_layer = get_channel_layer()
class NSEConsumer(AsyncWebsocketConsumer):
    # async def receive(self):
    #     print('in receive')
    #     nse=Nse()
    #     all = await database_sync_to_async(script.objects.values())
    #     for i in all:
    #         data = nse.get_quote(i['code'])
    #         if i['price'] > data['lastPrice']:
    #             i.update(state = 'up')
    #         if i['price'] > data['lastPrice']:
    #             i.update(state = 'do')
    #         if i['price'] > data['lastPrice']:
    #             i.update(state = 'un')
    #         i.update(price = data['lastPrice'])
    #         i.update(buy_quantity = data['buyQuantity1'])
    #         i.update(buy_price = data['buyPrice1'])
    #         i.update(sell_quantity = data['sellQuantity1'])
    #         i.update(sell_price = data['sellPrice1'])
    #         i.update(change = data['change'])
    #         i.update(change_percentage = round((data['change']*100)/data['lastPrice'],2))
    #         i.save()
    #     await self.send(text_data=json.dumps({
    #         'text': data,
    #         "type": "websocket.send",
    #     }))
    def update_data():
        print('in update data')
        nse=Nse()
        l=[]
        all = script.objects.values()
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
            i.update(change_percentage = round((data['change']*100)/data['lastPrice'],2))
            # i.save()
        l.append(data)
        async_to_sync(channel_layer.group_send)('stocks',{'type':'send_new_data','text': l})

    async def connect(self):  
        print('in connect')
        self.accept()
        await self.channel_layer.group_add('stocks', self.channel_name)
    async def disconnect(self,code):  
        print('in disconnect')
        await self.channel_layer.group_discard('stocks', self.channel_name)
    
    async def send_new_data(self,event):
        new_data = event['text']
        await self.send(text_data=json.dumps(new_data))

