# 22.01.2025
# vohidov
# While tsikli

# ism = input("Ismingiz nima? ")
# print(f'Salom, {ism.title()}')

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz

# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son += 1 # songa 1 qo'shamiz.

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)

# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# # infinite loop # bunda son o'zgarmaydi
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 0
# while son<10:    
#     if son%2!=0:
#         continue
#     else:
#         print(son)
#     son += 1 # ushbu qator while dan keyingi qatorda yozilishi kerak

# son = 1
# while son>0: # shartda son cheksizga qarab ketish sharti berilgan
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# print("Keling siz yaxshi ko'rgan kitoblar ro'yxatini yaratamiz!")
# savol = f"Kitob nomini kiriting "
# savol += f"(dasturni to'xtatish uchun 'stop' deb yozing):"
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if savol != 'stop':
#         print(qiymat.title())

# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         break
# print('Rahmat!')       

# print("Alisher Navoiy muzeyiga xushkelibsiz!")
# savol = "Yoshingizni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit' sozini kiriting): "
# yosh = ''
# while True:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     yosh = int(yosh)
#     if yosh < 7:
#         narh = 2000
#     elif yosh <= 18:
#         narh = 3000
#     elif yosh < 65:
#         narh = 10000
#     else:
#         narh = 0
#     print(f"Siz chipta narhi {narh} so'm")
  

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue 
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
