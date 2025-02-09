# 09.02.2025
# vohidov
# takrorlash

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

# salom_ber("shoxrux")

# print(salom_ber.__doc__)
# print(range.__doc__)

# salom_ber('hasan')
# salom_ber('olim')

# def toliq_ism(ism,familiya):
#     """ism va familiya qabul qilib komsulga chiqaradigan fuksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n")
#     print(f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism('shoxrux','vohidov')

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2025-tugilgan_yil} yoshda")

# # yosh_hisobla('shoxrux',2005)
# yosh_hisobla(tugilgan_yil=2005,ism='shoxrux')

# def yosh_hisobla(t_yil, j_yil=2025):
#     print(f"Siz {j_yil-t_yil} yoshdasiz!")

# yosh_hisobla(t_yil=2005)

# def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil =int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)

# def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1994)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim','hakimov')

# def toliq_ism_yasa(ism,familiya):
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism
# freegan = toliq_ism_yasa('shoxrux','vohidov')
# print(freegan)

# def toliq_ism_yasa(ism,familiya,otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism.title()} {otasining_ismi.title()} {familiya.title()}"
#     else:
#         toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism

# human = toliq_ism_yasa('shoxrux','vohidov')
# print(human)

# def avto_info(kampaniya,model,rangi,karobka,yili,narhi=None):
#     avto = {
#         "kampaniya":kampaniya,
#         "model":model,
#         "rang":rangi,
#         "karobka":karobka,
#         "yili":yili,
#         "narh":narhi}
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
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# a = oraliq(10,20)
# print(a)

# def avto_info(kampaniya,model,rangi,karobka,yili,narhi=None):
#     avto = {
#         "kampaniya":kampaniya,
#         "model":model,
#         "rang":rangi,
#         "karobka":karobka,
#         "yili":yili,
#         "narh":narhi}
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

# print("Salonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}. Narhi: {narh.title()}")

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()} bahosini kiriting: ")
#         baholar[ism] = baho
#     return baholar

# talabalar = ['ali','husan','hasan','vali']
# baholar = bahola(talabalar)
# print(baholar)

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(talabalar)

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(talabalar)

# def summa(*sonlar):
#     """Kiritilgan sonlarning yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0 
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,3,4,5,6))

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)
# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(4,5,6,7))

# def avto_info(kompaniya,model,**malumotlar):
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar

# avto1 = avto_info('GM','Matiz',narhi=2000,yili=2010)

# print(avto1)

# import math

# num = 400
# print(math.sqrt(num))

# print(pow(5,6))

# from math import pi

# print(pi)

# print(math.log2(8))
# print(math.log10(100))

# import random as r # random modulini r deb chaqirayapmiz

# # son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
# # print(son)

# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)
