# 23.01.2025
# vohidov
# WHILE, RO'YXATLAR VA LUG'ATLAR

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break

# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# car = 'nexia'
# while car in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove(car) # nexia ni ro'yxatdan olib tashla
# print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)

# amaliyot

# buyurtmalar  = []
# print("Xarid qilish uchun mahsulot tanlang")
# n=1
# while True:
#     buyurtma = f"{n}-mahsulot nomini kiriting:"
#     nom = input(buyurtma)
#     buyurtmalar.append(nom)
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break

# savat =[]
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
#     if javob != 'ha':
#         break

# print("Mahsulotlar narhini belgilaymiz")
# mahsulot_narhlari = {}
# ishora = True
# while ishora:
#     name = input("Mahsulot nomini kiriting:")
#     narh = input(f"{name.title()}ning narhini kiriting:")
#     mahsulot_narhlari[name] = int(narh)
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for name, value in mahsulot_narhlari.items():
#     print(f"{name.title()} {value} so'm") 

# mahsulotlar = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
#     mahsulotlar[mahsulot] = narh
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
#     if javob != 'ha':
#         break

# mahsulotlar = {
#     'olma':5000,
#     'nok':7000,
#     'shakar':15000,
#     'go\'sht':100000,
#     'non':4000,
#     'choy':3000,
#     'shirinlik':30000
# }

# savat = []
# print("Xarid qilish uchun mahsulot tanlang")
# n=1
# while True:
#     mahsulot = input(f"{n}-mahsulot nomini kiriting:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo;shasizmi? (ha/yo'q)")
#     n+=1
#     if javob != 'ha':
#         break

# for name in savat:
#     if name in mahsulotlar.keys():
#         narh = mahsulotlar[name]
#         print(f"\n{name.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {name.title()} yo'q")


# # 2-usul
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")
