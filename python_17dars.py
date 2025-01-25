# 24.01.2025
# vohidov
# funksiya

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber("shoxrux")
# # print(salom_ber.__doc__)
# salom_ber("abduqodir")

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
        
# toliq_ism("shoxrux","vohidov")

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2025-tugilgan_yil} yoshda")

# yosh_hisobla(tugilgan_yil=2005,ism="shoxrux")

# def yosh_hisobla(tugilgan_yil, joriy_yil=2025): # joriy yil uchun st.qiymat 2020
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(tugilgan_yil=2005)

# def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1993,2025)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim','hakimov')

# AMALIYOT

# def yosh_hisobla(ism,yosh):
#     """Foydalanuvchidan ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2025-yosh}-yilda tug'ilgan")
    
# ism = input("Ismingizni kiriting: ")
# yosh = int(input("yoshingizni kiriting: "))

# yosh_hisobla(ism=ism,yosh=yosh)

# def hisobla(son):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga, kubi esa {son**3} ga teng")
    
# son = int(input("Istalgan butun sonni kiriting:"))
# hisobla(son=son)

# def juf_toq(son):
#     """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son == 0:
#         print(f"{son} son 0 ga teng")
#     elif son%2 == 0:
#         print(f"{son} juft son")
#     elif son < 0:
#         print(f"{son} butun son emas")
#     elif son%2 != 0:
#         print(f"{son} toq son")

# son = int(input("Istalgan butun son kiriting: "))

# juf_toq(son)

# def katta_kichik_teng(num1, num2):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya."""  
#     """Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaruvchi fuksiya."""
#     if num1 > num2:
#         print(f"{num1} katta {num2} dan")
#     elif num1 == num2:
#         print(f"{num1} teng {num2} ga")
#     else:
#         print(f"{num2} katta {num1} dan")

# print("Ikkita butun sondan kattasini topuvchi dastur")    
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# katta_kichik_teng(num1=son1,num2=son2)

# def x_ning_y_darajasi(x,y=2):
#     """Foydalanuvchidan x va y sonlarini olib, x/y ni konsolga chiqaruvchi funksiya """
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")

# x = int(input("Sonni kiriting:"))
# y = int(input("Darajasini kiting: "))

# x_ning_y_darajasi(x, y)

# def bolinish_alomatlari(son):
#     """Foydalanuvchidan son qabul qilib, 
#     sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     for n in list(range(2,11)):
#         if son%n == 0:
#             print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# son = int(input("Istalgan butun son kiriting: "))
# bolinish_alomatlari(son=son)