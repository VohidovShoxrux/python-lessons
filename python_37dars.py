# 03.03.2025
# vohidov
# PYTHON STANDART KUTUBXONASI

# import datetime as dt 

# hozir = dt.datetime.now()

# print(hozir)

# print(hozir.date())

# print(hozir.time())

# print(hozir.hour) 

# print(hozir.minute)

# print(hozir.second)

# bugun = dt.date.today()

# print(f"Bugun sana: {bugun}")

# ertaga = dt.date(2025,3,4)
# print(f"Ertaga sana: {ertaga}")

# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")

# vaqtKeyin = dt.time(23,45,00)
# print(f"Bugun futbol soat: {vaqtKeyin}")

# bugun = dt.date.today()
# juma = dt.date(2025,3,7)
# farq = juma - bugun
# # print(farq)
# print(f"Jumaga {farq.days} kun qoldi")

# hozir = dt.datetime.now()
# futbol = dt.datetime(2025,3,4,23,45,00)
# farq = futbol-hozir
# sekundlar = int(farq.total_seconds())
# minutlar = int(sekundlar/60)
# soatlar = int(minutlar/60)
# print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
# print(f"Futbol boshlanishiga {minutlar} minut qoldi")
# print(f"Futbol boshlanishiga {soatlar} soat qoldi")

# hozir = dt.datetime.now()
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozir soat: {vaqt}")

# sana = hozir.strftime("%d-%m-%Y")
# print(f"Bugun sana: {sana}")

# sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
# print(sana_vaqt)

# import math
# PI = math.pi
# print(f"PI ning qoyimati: {PI}")

# E = math.e
# print(f"e ning qiymati: {E}")

# Trigonometriya

# print(math.sin(math.pi/2))
# print(math.cos(0))
# print(math.tan(PI))

# print(math.degrees(math.pi/2))
# print(math.radians(90))

# LOGARIFMLAR

# print(math.log2(8))
# print(math.log10(100))

# sonalar

# x = 4.51
# print(round(x))
# print(math.ceil(x))
# print(math.floor(x))

# x = 81
# a = 5
# b = 27
# print(math.sqrt(x))
# print(math.pow(a,3))
# print(math.pow(b,1/3))

# pprint moduli

# from pprint import pprint
# import json

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)

# pprint(bemor)

# RegEx

import re

# word1 = "stul"
# word2 = "stol"
# word3 = "saot"

# andoza = "^s..l$"
# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

from wordlist import words
# andoza = "^s..l$"

# matches = []
# for word in words:
#     if re.match(andoza,word):
#         matches.append(word)

# print(matches)

# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi: vohidovmillatumidvori01@gnail.com
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)
# print(email)

# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
# andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# msg = "Yangi parol kiriting"
# msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
# msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

# while True:
#     password = input(msg)
#     if re.match(andoza,password):
#         print("Maxfiy so'z qabul qilindi")
#         break
#     else:
#         print("Maxfiy so'z talabga javob bermadi")