# 3.11.2024
# vohidov
# LUG'AT ELEMENTLARI BILAN ISHLASH

# student = {
#     'name':'shoxrux',
#     'lastname':'vohidov',
#     'age':19,
#     'Faculty':'computer engineering',
#     'course':2
# }
# print(student.items())

# for key, value in student.items():
#     print(f"Key: {key.title()}")
#     print(f"Value {value}\n")

# products = {
#     'apple' : 10000,
#     'nut':20000,
#     'meat' : 30000,
#     'pomegranate' : 29000,
#     'tangerine' : 31000,
#     'pear' : 2000
# }

# print(products.keys())

# print('Do\'kondagi mahsulotlar: ')
# for mahsulot in products.keys():
#     print(f"{mahsulot.title()}")

# for mahsulot in products:
#     print(f"{mahsulot.title()}")

# bozorlik = ['apple', 'grape', 'pineapple', 'nut']

# for mahsulot in products:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {products[mahsulot]} $")

# for buyum in bozorlik:
#     if buyum not in products:
#         print(f"Iltmos, do'kong {buyum} ham olib keling")

# for mahsulot in sorted(products):
#     print(mahsulot.title())

# phones = {
#     '1ali':'iphone x',
#     'vali':'iphone 11 pro',
#     '1xasan':'iphone se',
#     'xusan':'iphone 13 pro max',
#      '2ali':'iphone x',
#     'vali':'iphone 11 pro',
#     '2xasan':'iphone se',
#     'xusan':'iphone 13 pro max',
#      '3ali':'iphone x',
#     'vali':'iphone 11 pro',
#     '3xasan':'iphone se',
#     'xusan':'iphone 13 pro max',
#      '4ali':'iphone x',
#     'vali':'iphone 11 pro',
#     '4xasan':'iphone se',
#     'xusan':'iphone 13 pro max',
# }
# print("Telefonlar jamlanmasi:")
# for tel in set(phones.values()):
#     print(tel)

# elements = {'11','12','12','13','14','11','13','14'}
# print(type(elements))

# Amalayot

# lugat = {
#     'adryu':'robertson',
#     'karlo':'anchelotti',
#     'cristiano':'ranaldo',
#     'cross':'benjamon',
#     'bahodir':'jalolov'
# }

# for key , value in sorted(lugat.items()):
#     print(f"{key.title()}-{value.title()}")
   
# countries = {
#     "uzbekistan":"Tashkent",
#     "russia":"Moscow",
#     "united states":"Washington",
#     "china":"Beijing",
#     "france":"Paris",
#     "united kingdom":"London",
#     "germany":"Berlin",
#     "japan":"Tokyo",
#     "india":"New Delhi",
#     "turkey":"Ankara",
# }

# print("Dunyo davlatlari:")
# for k in sorted(countries):
#     print(k.upper())

# print('\nDavlatlarning poytaxtlari:')
# for v in sorted(countries.values()):
#     print(v.title())

# country = input("What country do you want to know the capital of?:").lower()
# capital = countries.get(country)

# 1-yechim
# if capital == None:
#     print("Bizda bunday ma'lumot yo'q")
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shaxri")

# 2- yechim
# search = input("What country do you want to know the capital of?: ").lower()
# found = False  # Kalitni topilganligini belgilovchi o'zgaruvchi

# for country, capital in countries.items():
#     if search == country:  # Foydalanuvchi kiritgan davlatni tekshirish
#         print(f"{country.upper()}ning poytaxti {capital.title()}!")
#         found = True  # Kalit topilganda belgilash
#         break  # Qidirishni to'xtatish

# if not found:
#     print("Bizda bunday ma'lumot yo'q")

# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print('3 ta taom buyurtma bering.')
# orders = []
# for n in range(3):
#     orders.append(input(f"{n+1}-taom:").lower())

# for order in orders:
#     if order in menu:
#         print(f"{order.title()} {menu[order]} so'm ")
#     else:
#         print(f"Kechirasiz, bizda {order} yo'q")