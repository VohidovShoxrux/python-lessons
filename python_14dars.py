# 19.01.2025
# vohidov
# nesting

# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }
    
# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")  

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")

# print(cars[0])
# print(cars[0]['model'])
# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")

# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz

# for malibu in malibus[:3]:
#     malibu['rang']='qizil'

# for malibu in malibus[3:6]:
#     malibu['rang']='qora'

# for malibu in malibus[6:]: # ohirgi 4 ta mashinani
#     malibu['rang']='qora'  # rangi qora
#     malibu['korobka']='mexanika' # korobkasi mexanika

# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000
# print(malibus)

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
#     for til in tillar:
#         print(f'{til.upper()} ', end='')

# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper(), end=' ')

# shaxs1 = {
#     'ism':"alisher navoiy",
#     't_yil':1441,
#     't_joy':"Xirot",
#     'vafot':1501,
#     'meros':["Xamsa","Lison ut-tayr","Nasoyim ul-muhabbat","Mahbub ul-qulub "]
# }
# shaxs2 = {
#     'ism':'Jomiy',
#     't_yil':1414,
#     't_joy':"xirot",
#     'vafot':1492,
#     'meros':["Shavohid un-nubuvvat","Nafahot ul-uns min hazarot il-quds","Naqd un-nusus","Naqshbandiya "]
# }
# shaxs3 = {
#     'ism':"g'azzoliy",
#     't_yil':1058,
#     't_joy':"tus(eron)",
#     'vafot':1111,
#     'meros':["Bosit", "Vojiz", "Vosit","Maqosid al-falasifa"]
# }
# shaxs4 = {
#     'ism':"Bahouddin Naqshband",
#     't_yil':1318,
#     't_joy':"Buxoro",
#     'vafot':1389,
#     'meros':["Qomus al-alom","Hayotnoma","Daloyil ul-oshiqin","Avrod"]
# }

# shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]

# # for shaxs in shaxslar:
# #     print(f"\n{shaxs['ism'].title()} {shaxs['t_yil']}-yilda "
# #           f"{shaxs['t_joy'].capitalize()}da tavallud topgan. "
# #           f"{shaxs['vafot']-shaxs['t_yil']} yil umir ko'rgan",end= ' ')

# for ism in shaxslar:
#     print(f"\n{ism['ism'].title()} ning mashxur asarlari:")
#     for asar in ism['meros']:
#         print(asar.title())

# oila_azolar = {
#     'akam':['uzuklar hukumdori','garri potter','uyda yolg\'iz'],
#     'men':['interstellar','marvel studio','novda'],
#     'onam':['qodirxon','alahazar','kundosh'],
#     'opam':['qish stanatasi','zamonlar osha','osmondagi bolalar']
# }

# for ism, kino in oila_azolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for k in kino:
#         print(k.title())

# davlatlar = {
#     'o\'zbekiston':{
#         'poytaxt':'toshkent',
#         'hududi':448978,
#         'aholi':40000000,
#         'valyuta':'so\'m'
#     },
#     'rossiya':{
#         'poytaxt':'maskva',
#         'hududi':17098246,
#         'aholi':150000000,
#         'valyuta':'rubl'
#     },
#     'aqsh':{
#         'poytaxt':'vashington',
#         'hududi':9631418,
#         'aholi':350000000,
#         'valyuta':'dollar'
#     },
#     'malaziya':{
#         'poytaxt':'kuaval-lumpur',
#         'hududi':329750,
#         'aholi':25000000,
#         'valyuta':'rinngit'
#     }
# }

# davlat = input("Davlat nomini kiriting: ").lower()

# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['hududi']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['valyuta']}") 
# else:
#     print("Bizda bu davlat haqida ma'lumot yo'q" )
