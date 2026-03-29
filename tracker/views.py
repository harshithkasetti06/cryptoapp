import requests
from django.shortcuts import render

def home(request):
    coin = request.GET.get('coin', 'bitcoin')  # default bitcoin

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr"
    
    try:
        response = requests.get(url)
        data = response.json()

        price = data.get(coin, {}).get('inr', 'Not Found')

    except:
        price = "Error"

    context = {
        'coin': coin,
        'price': price
    }

    return render(request, 'tracker/index.html', context)