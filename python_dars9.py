# 27.10.2024
# vohidov
# BIR NECHTA SHARTLARNI TEKSHIRISH

# yosh = int(input("Yosshingizni kiriting:"))
# if yosh < 4:
#     narh = 0
# elif yosh < 12:
#     narh = 5000
# elif yosh < 18:
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} so'm")

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")

# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and harorat >= 30:
#     print("Cho'milishga ketdik")
# elif kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and harorat <= 30:
#     print("Uyda dam olamiz")

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = 1
# salat = 0
# non = 1
# kompot = 1 
# assorti = 1
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

# menu = [ 'osh', 'gumma', 'xonim', 'shashlik', 'norin']
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#     print('Buyurtmangiz qabul qilindi!')
# else:
#     print('Afsuski bizda nunday ovaqat yo\'q')

# menu = [ 'osh', 'somsa', 'manti', 'shashlik', 'pitsa', 'kola', 'fanta', 'shakarop', 'salat', 'choy']
# zakaz = ['osh', 'kola', 'ko\'k choy', 'manti']

# if zakaz:
#     for taom in zakaz:
#         if taom in menu:
#            print(f"Menuda {taom} bor")
#         else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
# else:
#     print("Savatingiz bo'sh!")


# Amaliyot

# juft = int(input("Juft son kiriting: "))
# if juft%2:
#     print("Bu son juft emas.")
# else:
#      print("Rahmat")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4 or yosh >= 60:
#     narx = 0
# elif yosh < 18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Sizga kirish {narx} so'm.")

# number1 = float(input("Birinchi sonni kiriting: "))
# number2 = float(input("Ikkinchi sonni kiriting: "))
# if number1 > number2:
#     print(f"{number1}>{number2}")
# elif number1 < number2:
#     print(f"{number1}<{number2}")
# else:
#     print(f"{number1}={number2}")

# mahsulotlar = ["kartoshka", "piyoz", "guruch", "go'sht", "sabzi", "yog'", "uzum", "shakar", "olma", "nok"]
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulot qo'shing: "))
# bor_mahsulot = []
# yoq_mahsulot = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#        bor_mahsulot.append(mahsulot)
#     else:
#         yoq_mahsulot.append(mahsulot)
# if yoq_mahsulot in mahsulotlar:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q {yoq_mahsulot}")

# users = ['karl', 'john', 'harry', 'jemis', 'klark', 'bob', 'jonson', 'jeni', 'anna', 'nina']
# login = input("Yangi login kiriting:")
# if login in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")