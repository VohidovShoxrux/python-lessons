# 10.11.2024
# vohidov
# WHILE TSIKLI

# ism = input("Ismingiz nima? ")
# savol =  f"Salom, {ism.title()}. Yoshingiz nechada? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Boyingiz necha metr? ")
# height = float(height)
# print(height)

# son = 1
# while son <=5:
#     print(son, end=' ')
#     son += 1
# print('Dastur tugadi!')

# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
# qiymat = ''
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dstur to\'xtadi!')

# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
# qiymat = ''
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dstur to\'xtadi!')

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)

# son = 0
# while son<10:
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
#     son += 1

# son = 1
# while son>0:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)

# while True:
#     kitob = input("Sizga yoqgan kitoblar nomini kiriting(dasturni to'xtatish uchun 'stop' so'zini kiriting!): ")
#     if kitob == 'stop':
#         break

# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!') 

# print("Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:")

# while True:
#     yosh = input("Yoshingizni kiriting:")
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     yosh1 = int(yosh)
#     if yosh1 < 7:
#         narh = 2000
#     elif 7 <= yosh1 < 18:
#         narh = 3000
#     elif 18 <= yosh1 < 65:
#         narh = 10000
#     else:
#         narh = 0
#     if narh == 0:
#         print('Sizga chipta bepul')
#     else:
#         print(f"Chipta {narh} so'm")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat.title()=='Exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")