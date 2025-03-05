# 05.04.2025
# vohidov
# requests

import requests
from pprint import pprint

# manzil = "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)

# country = "Brazil"
# url = f"https://restcountries.com/v3.1/name/{country}"
# r = requests.get(url)
# r_json = r.json()[0]
# print(r_json['capital'])

import googletrans
import asyncio 

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()['slip']['advice']
print(advice)

async def main():
    tarnslator = googletrans.Translator()
    tarjima = await tarnslator.translate(advice, dest='uz')
    print(tarjima.text)


asyncio.run(main())
