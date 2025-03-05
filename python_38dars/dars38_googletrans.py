# 05.04.2025
# vohidov
# googletrans

import asyncio 
from googletrans import Translator
tarjimon = Translator()
async def main():
    # matn_uz = "Tashkent is the capital of Uzbekistan"
    # tarjima = await tarjimon.translate(matn_uz, dest='uz')
    # print(tarjima.text)
    msg = "Tarjima uchun so'z kiriting (chiqish \"q\"):"
    while True:
        text = input(msg)
        if text == "q":
            break
        else:
            tarjima = await tarjimon.translate(text, dest='en')
            print(tarjima.text)

asyncio.run(main())

