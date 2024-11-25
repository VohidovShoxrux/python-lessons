# 13.11.2024
# vohidov
# FUNKSIYA

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()

# def salom_ber(ism):
#     """Foydalanuchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

# salom_ber('shoxrux')
# salom_ber('vohidiv')

# print(salom_ber.__doc__)
# print(print.__doc__)

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism('shoxrux','vohidov')

# def yosh_hisobla(ism, tuglgan_yil):
#     """Foydalanuvchi yoshini hisoblovchi dastur"""
#     print(f"{ism.title()} {2024-tuglgan_yil} yoshda")

# yosh_hisobla('shoxrux',2005)
# yosh_hisobla(tuglgan_yil=1997,ism='olim')

# def yosh_hisobla(tuglgan_yil, joriy_yil=2024):
#     """Foydalanuvchi yoshini hisoblovchi dastur"""
#     print(f"Siz {joriy_yil-tuglgan_yil} yoshdasiz")

# yosh_hisobla(2005,2024)
# yosh_hisobla(2005)

# Amaliyot

# print("3 ta son kiriting!")
# n = 1
# while True:
#     num1 = int(input(f"{n}-sonni kiriting:"))
#     n += 1
#     num2 = int(input(f"{n}-sonni kiriting:"))
#     n += 1
#     num3 = int(input(f"{n}-sonni kiriting:"))
#     if num1 > num2:
#         if num1 > num3:
#             print(f"{num1}=max")
#             if num2 > num3:
#                 print(f"{num3}=min")
#             else:
#                 print(f"{num2}=min")
#         else: 
#             print(f"{num3}=max")
#             print(f"{num2}=min")
#     elif num1 == num2:
#         if num1 > num3:
#            print(f"{num3}=min")
#            print(f"{num1}={num2}")
#         elif num1 == num3:
#              print(f"{num1}={num2}={num3}")
#         else:
#             print(f"{num3}=max")
#             print(f"{num1}={num2}")
#     elif num2 > num3:
#         print(f"{num2}=max")
#         if num1 > num3:
#             print(f"{num3}=min")
#         elif num1 == num3:
#             print(f"{num1}={num3}")
#         else:
#             print(f"{num1}=min")
#     else:
#         print(f"{num3}=max")
#         print(f"{num1}=min")
   
#     savol = input("Damvom etasanmi? (ha/yoq)")
#     n = 1
#     if savol != 'ha':
#         break

# def yosh_hisobla(ism, tuglgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2024-tuglgan_yil} yoshda")

# def hisobla(son):
#     """Foydalanuvchidan son qabul qilib uni kvadrati, kubini hisoblovchi dastur"""
#     print(f"{son} ning kvadrati {son**2} ga teng\n"
#           f"{son} ning kubi {son**3} ga teng")

# num = int(input("Son kiriting:"))
# hisobla(num)

# def hisobla(son):
#     '''Foydalanuvchidan son qabul qilib uni juft yoki toq ekanligini aniqlovchi function'''
#     if son%2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")

# number = int(input("Son kiriting:"))
# hisobla(number)

# def hisob(num1, num2):
#     """Ikki sondan katta va kichigini topuvchi funksiya"""
#     if num1 > num2:
#         print(f"birinchi son katta {num1}>{num2}")
#     elif num2 > num1:
#         print(f"ikkinchi son katta {num2}>{num1}")
#     else:
#         print(f"sonlar teng {num1}={num2}")

# print("Ikkita son kiriting va qasi biri katta yoki kichik ekaniligini ko'rsiz")
# son1 = int(input("Birinchi sonni kiriting:"))
# son2 = int(input("Ikkinchi sonni kiriting:"))
# hisob(num1=son1, num2=son2)

# def xisob(x, y=2):
#     print(f"{x} ning {y} darajasi {x**y} ga teng")

# print("ikkita son kirit:")
# num1 = int(input("x uchun son kiriting:"))
# num2 = int(input("y uchun son kiriting:"))
# xisob(x=num1, y=num2)

# def bolinish(son):
#     for  n in range(1,11):
#         if not  son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
# number = int(input("Son kiriting:"))
# bolinish(number)

