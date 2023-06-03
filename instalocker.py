from valclient.client import Client
import json
import time
import requests
import sys

#JSON verileri
url = "https://raw.githubusercontent.com/Burak35Smoke/Valorant-Instalock/main/data.json"
request = requests.get(url)
veri = json.loads(request.text)

#Değişken atamaları
ajanlar = veri['agents']
bolge = veri['region']
hoverDelay = veri['hoverDelay']
lockDelay = veri['lockDelay']
loopDelay = veri['loopDelay']

#API bağlantı
try:
    client = Client(region=bolge)
    client.activate()
except:
    print("Valorant'ı açın!")
    time.sleep(5)
    sys.exit()

#Kullanıcı girdileri ve ajan sorguları
start = input("Lütfen ajan ismi yazınız: ").lower()
print("Oyun bekleniyor.")

def karakterBilgisi():
    global start
    if start == 'astra':
        start = ajanlar['astra']
    elif start == 'breach':
        start = ajanlar['breach']
    elif start == 'brimstone':
        start = ajanlar['brimstone']
    elif start == 'chamber':
        start = ajanlar['chamber']
    elif start == 'cypher':
        start = ajanlar['cypher']
    elif start == 'fade':
        start = ajanlar['fade']
    elif start == 'gekko':
        start = ajanlar['gekko']
    elif start == 'harbor':
        start = ajanlar['harbor']
    elif start == 'jett':
        start = ajanlar['jett']
    elif start == 'kayo':
        start = ajanlar['kayo']
    elif start == 'killjoy':
        start = ajanlar['killjoy']
    elif start == 'neon':
        start = ajanlar['neon']
    elif start == 'omen':
        start = ajanlar['omen']
    elif start == 'phoenix':
        start = ajanlar['phoenix']
    elif start == 'raze':
        start = ajanlar['raze']
    elif start == 'reyna':
        start = ajanlar['reyna']
    elif start == 'sage':
        start = ajanlar['sage']
    elif start == 'skye':
        start = ajanlar['skye']
    elif start == 'sova':
        start = ajanlar['sova']
    elif start == 'viper':
        start = ajanlar['viper']
    elif start == 'yoru':
        start = ajanlar['yoru']

karakterBilgisi()

#API'den sorgu ve işlemlerin gerçekleştirilmesi
while True:
    time.sleep(loopDelay)
    try:
        oyuncuBilgisi = client.fetch_presence(client.puuid)['sessionLoopState']
        macBilgisi = client.pregame_fetch_match()['ID']
        if oyuncuBilgisi == "PREGAME":
            client.pregame_select_character(start)
            time.sleep(lockDelay)
            client.pregame_lock_character(start)
            print("Karakter kilitlendi.")
            break
    except:
        continue