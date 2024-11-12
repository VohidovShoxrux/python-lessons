# 12.11.2024
# vohidov
# while va ro'yxatlar

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"\n{n}-do'stingizni ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("\nYana qo'shishni istaysizmi? (ha/yo'q)")
#     n += 1
#     if takrorlash != 'ha':
#         break

# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini sqalaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("\nDo'stingizni ismini kiriting: ")
#     yosh = input(f"\n{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("\nYana ma'lumot qo'shasizmi? (ha/yo'q): ")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia','lacetti']
# car = 'lacetti'
# while car in cars:
#     cars.remove(car)

# print(cars)

# students = ['najim','jonibek','karl','hoshim']
# score_students = {}
# while students:
#     student = students.pop()
#     score = input(f"{student.title()}ning bahosini kiriting: ")
#     print(f"{student.title()} baholandi")
#     score_students[student] = int(score)

# Amalyoti

# print("Mahsulot uchun buyurtma berish.")
# buyurtmalar = []
# n = 1
# while True:
#     zakaz = f"\n{n}-buyurtmangizni nomini kiriting: "
#     name = input(zakaz)
#     buyurtmalar.append(name)
#     takrorlash = input("\nYana mahsulot qo'shishni istaysizmi? (ha/yoq) ")
#     n += 1
#     if takrorlash != 'ha':
#         break

# print("Buyurtmalaringiz ro'yxati:")
# for n in buyurtmalar:
#     print(n.title())

# print("Mahsulot narxlarini belgilash dasturi.")
# e_bozor = {}
# ishora = True
# while ishora:
#     name = input("\nMahsulot nomini kiriting: ")
#     cost = input(f"\n{name.title()}ning narxini kiriting: ")
#     e_bozor[name] = int(cost)
#     response = input("\nYana mahsulot qoshishni istaysizmi? (ha/yoq) ")

#     if response != 'ha':
#         ishora = False

# for name, cost in e_bozor.items():
#     print(f"{name.title()} = {cost}")

# zakazlar = ['olma','banan','shaftoli','behi','anjir']
# mahsulotlar = {
#     'olma':10000,
#     'behi':5000,
#     'nok':3200,
#     'shaftoli':17000,
#     'banan':3000
# }

# while zakazlar:
#     zakaz = zakazlar.pop()
#     if zakaz in mahsulotlar.keys():
#         price = mahsulotlar[zakaz]
#         print(f"\n{zakaz.title()} - {price} so'm ")
#     else:
#         print(f"""\nBizda "{zakaz}" yo'q""")