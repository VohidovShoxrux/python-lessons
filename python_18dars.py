# 30.01.2025
# vohidov
# QIYMAT QAYTARUVCHI FUNKSIYA

# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')

# print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talaba2.title()}")

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# def oraliq(min,max,qadam=1):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# # print(oraliq(0,10))
# # print(oraliq(10,21))
# print(oraliq(0,21,2)) # 0 dan 21 gacha 2 qadam bilan


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}. Narhi: {narh.title()}")

# amaliot

# def user_data(ism,familiya,t_yil,t_joy,email,phone):
#     data = {"ism":ism,
#             "familiya":familiya,
#             "age":2025-int(t_yil),
#             "t_joy":t_joy,
#             "email":email,
#             "phone":phone}
#     return data

# print("Iltimos shaxsingiz haqida ma'lumotlarni to'ldiring!")
# mijozlar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     ism=input("Ismingizni kiriting: ")
#     familiya=input("Familiyangizni kiriting: ")
#     yosh=input("Tug'ilgan yilingizni kiriting: ")
#     t_joy=input("Tug'ilgan jongizni kiriting: ")
#     email=input("Emailingiz nomini kirting: ")
#     phone=input("Telefon raqamingizni kiriting: ")

#     mijozlar.append(user_data(ism=ism,familiya=familiya,t_yil=yosh,t_joy=t_joy,email=email,phone=phone))

#     javob = input("Yana user qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# print("Mijozlar haqida ma'lumotlar: ")
# for mijoz in mijozlar:
#     if mijoz['phone']:
#         phone = mijoz['phone']
#     else:
#         phone = "Noma'lum"
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}\n{mijoz['age']} yoshda {mijoz['t_joy'].capitalize()} da tug'ilgan.\nAmaldagi email:{mijoz['email']} va tel raqami {phone}"  )

# def uch_son(a,b,c):
#     if a>b:
#         if a>c:
#             son = a
#         else:
#             son = c
#     else:
#         if b>c:
#             son = b
#         else:
#             son = c
#     return c

# print("Uchta sondan kattasini topuvchi dastur!")
# while True:
#     num1=int(input("Birinchi sonni kiriting: "))
#     num2=int(input("Ikkinchi sonni kiriting: "))
#     num3=int(input("Uchinchi sonni kiriting: "))
#     son = uch_son(a=num1,b=num2,c=num3)
#     print(f"Eng katta son {son}")

#     javob = input("Yana davom etamizmi? (yes/no)")
#     if javob == 'no':
#         break


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

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar

# print(fibonacci(10))

