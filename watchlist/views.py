from django.shortcuts import render
import requests, json
from nsetools import Nse
from .models import script
# Create your views here.
def watchlist_view(request):    
    nse=Nse()
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
    context ={'all':all,}
    return render(request=request,
                  template_name="watchlist/markets-light.html",
                  context=context)

