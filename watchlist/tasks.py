from asgiref.sync import async_to_sync
from nsetools import Nse
from channels.layers import get_channel_layer
channel_layer = update_data()
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
        i.save()
        l.append(data)
    async_to_sync(channel_layer.group_send)('stocks',{'type':'send_new_data','text': l})
        