# 18.01.2025
# vohidov
# Lug'at bilan ishlash

# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# # print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar:")    
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# print(telefonlar.values())
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)
    
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)

# amaliyot

# python_lugat = {
#     'if':"shart operatori",
#     'for':"loop yoki tsikl",
#     'integer':"butun sonlar",
#     'float':"o'nlik sonlar",
#     'string':"matn ma'lumot turi",
#     'list':"ro'yxat ma'lumot turi",
#     'tuple':"o'zgarmas ro'yxat",
#     'boolen':"mantiqiy ma'lumot turi",
#     'function':"funksiya",
#     'method':"metod"
# }
# n = 0
# for key,value in python_lugat.items():
#     n += 1
#     print(f"{n}.{key.title()} - {value.capitalize()}")

# countries = {
#     'AQSH':"Vashington, D.C.",
#     'Fransiya':"Parij",
#     'Germaniya':"Berlin",
#     'Rossiya':"Moskva",
#     'Xitoy':"Pekin",
#     'Braziliya':"Brasilia",
#     'Indiya':"Naypido",
#     'Italiya':"Rim",
#     'Turkiya':"Anqara",
#     'Yaponiya':"Tokiyo"
# }
# print(f"Dunyo davlatlari:")
# for key in sorted(countries.keys()):
#     print(key.upper())

# print("Dvalatlarning poytaxtlari")
# for value in sorted(countries.values()):
#     print(value)

# country = input("Qaysi davlatning poytaxtini bilish istaysiz?:")
# capital =  countries.get(country)
# if capital:
#     print(f"{country}ning poytaxti {capital} shaxri")
# else:
#     print("Bizda bunday ma'lumot yo'q")

# menu = {
#     'osh':15000,
#     'lag\'mon':20000,
#     'non':5000,
#     'xonim':3000,
#     'gumma':5000,
#     'somsa':3000,
#     'choy':2000,
#     'sharbat':7000,
#     'shashlik':20000
# }
# print("3 ta taom buyurtma bering.")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")
