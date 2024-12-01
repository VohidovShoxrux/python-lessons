# 27.11.2024
# vohidov
# Funksiyadan qiymat qaytarish

# def toliq_ism_yasya(ism, familya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familya}"
#     return toliq_ism

# talaba = toliq_ism_yasya("shoxrux", "vohidov")

# print(talaba)

# def toliq_ism_yasya(ism, familya, otasini_ismi=''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasini_ismi:
#         toliq_ism = f"{ism} {otasini_ismi} {familya}"
#     else:
#         toliq_ism = f"{ism} {familya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasya('shoxrux','vohidov')
# talaba2 = toliq_ism_yasya('shoxrux','rasvshanbek o\'g\'li','vohidov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#     avto = { 'kompaniya': kompaniya,
#              'model': model,
#              'rangi': rangi,
#              'karobke': karobka,
#              'yili': yili,
#              'narh': narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','qora','avtomat', 2020)
# avto2 = avto_info('GM','Gentra','qora','mehanika', 2023, 15000)
# avtolar = [avto1, avto2]
# print('Online bozordagi mavjud avtomashinalar:')
# for  avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rangi']} {avto['model']}. Narhi:{narh}")

# def oraliq(min,max,qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(0,10,3))
# print(list(range(0,10,3)))

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#     avto = { 'kompaniya': kompaniya,
#              'model': model,
#              'rangi': rangi,
#              'karobke': karobka,
#              'yili': yili,
#              'narh': narhi}
#     return avto

# print("Saytimizda avtolar ro'yxatini shakillantiramiz.")
# avtolar = []
# while True:
#     print("\nQuydagi ma'lumotlarni kiriting\n")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     karobka=input("Karobkasi: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")

#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))

#     javob = input("Yana avto qoshasizmi? (yes/no): ")
#     if javob =='no':
#         break

# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rangi'].title()} {avto['model']}, {karobka} karobka. Narhi: {narh}")

# Amaliyot

# def user_data(name,lastname,age,where,email,phone_number):
#     user = {"ism":name,
#             "familya":lastname,
#             "yosh":age,
#             "t_joy":where,
#             "elektronpochta":email,
#             "tel_nomer":phone_number}
#     return user

# print("Foydalanuvchi ma'lumotlari.")
# users = []
# while True:
#     print("Quydagi ma'lumotlarni kiriting.\n")
#     ism = input("Ismingizni kiriting: ")
#     familya = input("Familyangizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))
#     t_joy = input("Tug'ilgan joyingini kiriting: ")
#     elektronpochta = input("Elektron pochta manzilini kiriting: ")
#     tel_raqam = input("Telefon raqamingizni kiriting: ")
    
#     users.append(user_data(ism,familya,yosh,t_joy,elektronpochta,tel_raqam))

#     savol = input("Yana boshqa user ma'lumotlari qo'shasizmi? (yes/no): ")
#     if savol == 'no':
#         break

# print("\nFoydalanuvchi ma'lumotlari.")
# for user1 in users:
#     if user1['tel_nomer']:
#         number = user1['tel_nomer']
#     else:
#         number = "unkonwn"
#     print(f"{user1['ism'].title()} {user1['familya'].title()}, {2024-user1['yosh']}-yil {user1['t_joy'].title()}da tug'ilgan!"
#           f"\nElektron pochta manzili: {user1['elektronpochta']}\nTelefon raqami: {number}\n")

# def maximum(x,y,z):
#     # bu funksiyada faqat turlicha sonlar kiritish talab qilinadi va faqat eng katta sonni qaytaradi
#     if x>y:
#         if x>z:
#             maximum1 = x
#         else:
#             maximum1 = z
#     elif y>x:
#         if y>z:
#             maximum1 = y
#         else:
#             maximum1 = z
#     return maximum1

# a = maximum(2,3,5)
# print(a)

# def aylana(r):
#     pi = 3.14
#     doira = {"radiusi":r,
#              "diametri":2*r,
#              "perimetri":2*pi*r,
#              "yuzi":pi*(r**2)}
#     return doira

# a = aylana(4)
# print(a)

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar

# a = tub_sonlar_top(1,10)
# print(a)

# def fibanachi(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2]) 
#     return sonlar
    
# print(fibanachi(10))
