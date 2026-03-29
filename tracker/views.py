import requests
from django.shortcuts import render

def home(request):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=inr"
    response = requests.get(url)
    data = response.json()

    context = {
        'bitcoin': data['bitcoin']['inr'],
        'ethereum': data['ethereum']['inr'],
        'dogecoin': data['dogecoin']['inr'],
    }

    return render(request, 'tracker/index.html', context)