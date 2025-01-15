# 12.01.2025
# vohidov
# if-elif-else

# yosh = int(input("Yoshingiz nechada? "))
# if yosh<=4:
#     print("Sizga kirish bepul.")
# elif yosh<=12:
#     print("Sizga kirish 5000 so'm")
# elif yosh<=18:
#     print("Sizga kirish 8000 so'm")
# else:
#     print("Sizga 10000 so'm")

# yosh = int(input("Yoshingiz nechada? "))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<=18:
#     price = 8000
# else:
#     price = 10000
# print(f"Sizga kirish narhi {price} so'm")

# yosh = int(input("Yoshingizni kiriting? "))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# else:
#     price = 8000
# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000    
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='yakshanba' or kun.lower()=='shanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")
# else:
#     print("Bugun ishga boramiz")

# narh = 15000
# salat = 1
# choy = 1
# if salat and choy:
#     narh = narh + 10000
# elif salat or choy:
#     narh = narh + 5000
# else:
#     narh = narh
# print(f"Jami {narh} so'm")

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 0
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# if 'osh' in menu:
#     print("osh bor") 

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")

# amalyot

# son = int(input("Juft son kiriting: "))
# if son%2 == 0:
#     print("rahmat!")
# else:
#     print("Bu son juft emas.")

# yosh = int(input("Yoshingiz nechada?>>>"))
# if yosh<=4:
#     price = 0
# elif yosh<=18:
#     price = 10000
# elif yosh <60:
#     price = 20000
# else:
#     price = 0
# print(f"Sizga kirish {price} so'm")

# num1 = float(input("Birinichi sonni kiriting: "))
# num2 = float(input("Ikkinchi sonni kiriting: "))
# if num1>num2:
#     print(f"{num1}>{num2}")
# elif num1<num2:
#     print(f"{num1}<{num2}")
# else:
#     print(f"{num1}={num2}")

# maxsulotlar = ['non','shakar','tuz','gugurt','kartoshka','piyoz','sabzi','olma','qahva','yog\'']
# savat = []
# for n in range(5):
#     savat.append(input(f"\nSavatga {n+1}-maxsulotni qo'shing: "))

# for maxsulot in savat:
#     if maxsulot in maxsulotlar:
#         print(f"Do'konimizda {maxsulot} bor")
#     else:
#         print(f"Do'konimizda {maxsulot} yo'q ")

# maxsulotlar = ['non','shakar','tuz','gugurt','kartoshka','piyoz','sabzi','olma','qahva','yog\'']
# savat = []
# for n in range(5):
#     savat.append(input(f"\nSavatga {n+1}-maxsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for maxsulot in savat:
#     if maxsulot in maxsulotlar:
#         bor_mahsulotlar.append(maxsulot)
#     else:
#         mavjud_emas.append(maxsulot)
# if not mavjud_emas:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print("Quyidagi mahsulotlar do'konimizda yo'q:")
#     for maxsulot in mavjud_emas:
#         print(maxsulot)
    
# foydalanuvchilar = ['zahro','fuzayl','hamza','zubayir','muhammadsiddiq']
# login = input("Yangi login tanlang: ")

# if login.lower() in foydalanuvchilar:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")


# son = int(input("Istalagan butun sonni kiriting: "))
# for n in range(2,11):
#     if not son%n:
#           print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
