# 25.02.2025
# vohidov
# xatolar bilan ishlash

# yosh = input("Yoshingizni kiriting:")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {2025-yosh} yilda tug'ilgansiz")

# # ZeroDivisionError
# x,y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")

# mevalar = ['uzum','olma','anor','nok']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

# user = {
#     "username":"karl",
#     "status":"admin",
#     "email":"karl@gamil.com",
#     "phone":932142805
# }
# key = 'tel'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas")

# filename = "malumot.txt" # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"{filename} mavjud emas")

# import json
# files = ['talaba1.json','talaba5.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         pass        # print(f"{filename} mavjud emas")
#     else:
#         print(talaba['ism'])

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
# else:
#     print(f"x={x}")

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2025-yosh} yilda tug'ilgansiz") 

# amaliyot 

# try:
#     x = int(input("son kiriting: "))
#     y = int(input("yana son kiriting: "))
#     print(x, "/", y, "=", x / y)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# except ValueError:
#     print("Bu son emas")
# except:
#     print("Xato yuz berdi!")

# print("x/y hisoblovchi dastur")
# while True:
#     x = input("x ni kiriting: ")
#     if x.isdigit():
#         x = int(x)
#     else:
#         print("Bu son emas!")
#         continue

#     y = input("y ni kiriting: ")
#     if y.isdigit():
#         y = int(y)
#     else:
#         print("Bu son emas!")
#         continue

#     if y == 0:
#         print("y 0 bo'lishi mumkin emas!")
#         continue
#     else:
#         print(x, "/", y, "=", x / y)
#         break