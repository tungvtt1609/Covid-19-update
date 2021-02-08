import requests
from win10toast import ToastNotifier
import json
import time
def update():
    request=requests.get('https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true')
    data=request.json()
    text=f'Total: {data["infected"]} \nBeing treated: {data["treated"]} \nRecovered: {data["recovered"]} \nDeceased: {data["deceased"]} '

    while True:
        t=ToastNotifier()
        t.show_toast("Covid-19 of VietNam", text, duration=20)
        time.sleep(60)
update()
