# 14.02.2025
# vohidov
# OOP introduction

# x = 10
# print(type(x))

# matn = 'salom'
# print(type(matn))

# def salom_ber():
#     print("Assalamu alaykum!")

# print(type(salom_ber))

# matn = "salom"
# print(matn.upper())

# class Talaba:
#     """Talaba nomli klass"""
#     def __init__(self, ism, familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"

#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tug'ilganman"

# talaba1 = Talaba("Shoxrux","Vohidov",2005)
# # print(talaba1.ism)
# # print(talaba1.familiya)
# talaba2 = Talaba("Fuzayil","Ravshanbekov",2027)
# talaba3 = Talaba("Zahro","Ravshanbekovna",2029)
# # print(talaba2.ism)
# # print(talaba3.ism)

# # print(talaba2.tanishtir())
# print(talaba3.get_name())

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self,yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil
    
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

# talaba = Talaba("Shoxrux","Vohidov",2005)
# print(talaba.get_age(2025))

# class User:
#     def __int__(self,name,username,email):
#         self.name = name
#         self.uname = username
#         self.mail = email

#     def describe():
#         pass

#     def get_email():
#         pass

# amaliyot

# class User:
#     def __init__(self,ism,foydalanuvchi,eamil,tel_nomer):
#         self.name = ism
#         self.username = foydalanuvchi
#         self.email = eamil
#         self.phone_number = tel_nomer
    
#     def info(self):
#         return f"Username: {self.username}\nName: {self.name}\nEmail: {self.email}\nNumber: {self.phone_number}"

# user = User("Shoxrux","Karl","vohidovmillatumidvori01@gamil.com",932142805) 

# # print(user.username)
# print(user.info())
