# 8.11.2024
# vohidov
# NESTING
# car0 = {
#     'model':'gentra',
#     'rang':'qora',
#     'yil':2023,
#     'yurgan':130000,
#     'karobka':'avtomat',
#     'narh':15000
# }

# car1 = {
#     'model':'L9',
#     'rang':'olabula',
#     'yil':2024,
#     'yurgan':1001,
#     'karobka':'avtomat',
#     'narh':30000
# }

# car2 = {
#     'model':'L7',
#     'rang':'qizil',
#     'yil':2022,
#     'yurgan':1001001,
#     'karobka':'avtomat',
#     'narh':25000
# }

# cars = [car0, car1 ,car2]

# for car in cars:
#     print(f"{car['model'].title()}, " 
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$"    
#     )

# print(cars[1]['model'])

# l9 = []

# for n in range(10):
#     new_car = {
#         'model':'L9',
#         'rang':None,
#         'yil':2024,
#         'narh':None,
#         'km':0,
#         'karobka':'avto'
#     }
#     l9.append(new_car)

# for l in l9:
#     print(l)

# for n in l9[:3]:
#     n['rang'] = 'qizil'

# for n in l9[3:6]:
#     n['rang'] = 'qora'

# for n in l9[6:]:
#     n['rang'] = 'qora'
#     n['karobka'] = 'mexanika'

# for n in l9:
#     if n['karobka'] == 'avto':
#         n['narh'] = 40000
#     else:
#         n['narh'] = 30000

# for l in l9:
#     print(l)

# dasturchilar = {
#     'ali':['c++','python'],
#     'vali':['c#','.NET'],
#     'hasan':['java','php'],
#     'husan':['js','css','html'],
#     'fuzayil':['kotlin','Ruby']
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()}")

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()} ", end=' ')

# colleague = {
#     'ali':{
#         'familya':'valiyev',
#         'tyil':1995,
#         'malumot':'oliy',
#         'tillar':['python', 'c#']
#     },
#     'vali':{
#         'familya':'aliyev',
#         'tyil':1993,
#         'malumot':'o\'rta maxsus',
#         'tillar':['html','css','java']
#     },
#     'hasan':{
#         'familya':'husanov',
#         'tyil':1991,
#         'malumot':'maxsus',
#         'tillar':['python','php']
#     }
# }

# for ism, info in colleague.items():
#     print(
#         f"\n{ism.title()} {info['familya'].title()}, "
#         f"{info['tyil']}-yilda tug'ilgan. "
#         f"Ma'lumoti: {info['malumot']}. \n"
#         "Quydagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())

# Amalyot

# shaxs0 = {
#     'ism':'Erkin Vohidov',
#     'tyil':1936,
#     'tjoy':'Fargonada',
#     'umr':80,
#     'faoliyat':['shoir','o\'qituvchi ','jurnalist']
# }

# shaxs1 = {
#     'ism':'cristiano ronaldo',
#     'tyil':1985,
#     'tjoy': 'Portugaliyada',
#     'umr':'trik',
#     'faoliyat':['5 ta oltin to\'p','5 karra UEFA chempioni','2016 Yevropa chempioni']
# }

# shaxs2 = {
#     'ism':'Elon Musk',
#     'tyil':1971,
#     'tjoy':'Janubiy Afrikada',
#     'umr':'trik',
#     'faoliyat':['PayPal','SpaceX','Tesla','Neuralink']
# }

# shaxs3 = {
#     'ism':'Albert Eynshteyn',
#     'tyil':1879,
#     'tjoy':'Germaniyada',
#     'umr':76,
#     'faoliyat':['Nisbiylik nazariyasi','Fotoelektrik effekt','Brown harakati']
# }

# shaxslar = [ shaxs0, shaxs1, shaxs2, shaxs3]

# for n in shaxslar:
#     if n['umr'] != 'trik':
#         print(f"{n['ism'].title()} {n['tyil']}-yilda {n['tjoy'].title()} tavvalud topgan. {n['umr']} yil yashagan.")
#     else:
#         print(f"{n['ism'].title()} {n['tyil']}-yilda {n['tjoy'].title()} tavvalud topgan. Hozircha {n['umr']}")

# for n in shaxslar:
#     faoliyat = n['faoliyat']
#     print(f"{n['ism'].title()} ning faoliyat:")
#     for m in faoliyat:
#         print(m.capitalize())

# kino = {
#     'Akam':['Uyda yolg\'iz','Uzuklar hukumdori','Garri Potter','Osmandagi bolalar'],
#     'Men':['Interstellar','Boshqotirma','Snayper'],
#     'Opam':['Novda','Samo farzandlari','Loyqalangan suv']
# }

# for k, v in kino.items():
#     print(f"{k}ning sevimli kinolari:")
#     for n in v:
#         print(n)

# countries = {
#     'uzb':{
#         'poytaxt':'toshkent',
#         'hududi':448.900,
#         'aholi':37,
#         'pul':"so'm"
#     },
#     'poland':{
#         'poytaxt':'varshava',
#         'hududi':312.696,
#         'aholi':38,
#         'pul':'zloty'
#     },
#     'israel':{
#         'poytaxt':'tel-aviv',
#         'hududi': 22.072,
#         'aholi': 9,
#         'pul':'shekel'
#     }
# }

# for country, value in countries.items():
#     if country.lower() == 'uzb':
#         country = country.upper()
#     else:
#         country = country.capitalize()
#     print(f"\n{country}ning poytaxti {value['poytaxt'].title()}"
#           f"\nHududi: {value['hududi']} kv.km"
#           f"\nAholisi: {value['aholi']} mln"
#           f"\nPul birligi: {value['pul']}"
#     )

# country = input("Davlat nomini yoki qisqartmasini kiriting: ").lower()

# if country in countries:
#     info = countries[country]
#     print(f"\n{country.title()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['hududi']} kv.km"
#           f"\nAholisi: {info['aholi']} mln"
#           f"\nPul birligi: {info['pul']}"
#         )
# else:
#     print("Bizda bu davlat haqida ma'lumot yo'q")
   