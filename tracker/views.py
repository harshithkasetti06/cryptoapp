import requests
from django.shortcuts import render

def home(request):
    query = request.GET.get('coin', 'bitcoin')

    try:
        # 🔍 Search coin
        search_url = f"https://api.coingecko.com/api/v3/search?query={query}"
        search_res = requests.get(search_url).json()

        if search_res['coins']:
            coin_id = search_res['coins'][0]['id']
        else:
            coin_id = None

        if coin_id:
            # 📊 FULL DATA API
            url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
            data = requests.get(url).json()

            price = data['market_data']['current_price']['inr']
            high_24h = data['market_data']['high_24h']['inr']
            low_24h = data['market_data']['low_24h']['inr']
            market_cap = data['market_data']['market_cap']['inr']
            change_24h = data['market_data']['price_change_percentage_24h']

        else:
            price = high_24h = low_24h = market_cap = change_24h = "Not Found"

    except:
        price = high_24h = low_24h = market_cap = change_24h = "Error"

    return render(request, 'tracker/index.html', {
        'coin': query,
        'price': price,
        'high_24h': high_24h,
        'low_24h': low_24h,
        'market_cap': market_cap,
        'change_24h': change_24h,
    })