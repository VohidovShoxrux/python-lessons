# 15.02.2025
# vohidov
# VORISLIK VA POLIMORFIZM

# class Shaxs:
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}."
#         info +=f" Passport:{self.passport}, {self.tyil}-yilida tug'ilgan"
#         return info
    
#     def get_age(self,yil):
#         return yil-self.tyil

# inson = Shaxs("Hasan","Alimov","FB001122",1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")

# class Manzil:
#     def __init__(self,uy,kocha,tuman,viloyat):
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil



# class Talaba(Shaxs):
#     def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
#         super().__init__(ism,familiya,passport,tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
#         self.fanlar=[]
    
#     def get_id(self):
#         return self.idraqam

#     def get_bosqich(self):
#         return self.bosqich

#     def get_info(self):
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info

# talaba = Talaba("Shoxrux","Vohidov","FA112299",2005)
# print(talaba.get_info())

# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")

# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")

# print(f"{talaba.get_bosqich()}-bosqich talabasi")

# print(talaba.get_info())

# talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)

# print(talaba.manzil.get_manzil())

# print(talaba.manzil.get_info())

# print(talaba.manzil.tuman)

# amaliyot

# class Fan:
#     def __init__(self,nom):
#         self.nom = nom
    
#     def get_nom(self):
#         return self.nom


# class Talaba():
#     def __init__(self,ism,familiya):
#         self.ism = ism
#         self.familiya = familiya
#         self.fanlar = []

#     def get_info(self):
#         info = f"{self.ism} {self.familiya}"
#         info += f"{self.get_bosqich}-bosqich. ID raqam: {self.get_id}"

#     def fanga_yozil(self,fan):
#         if fan not in self.fanlar:
#             self.fanlar.append(fan)
#             return (f"{self.ism} {fan.nom} faniga yozildi.")
#         else:
#             return (f"{self.ism} allaqachon {fan.nom} faniga yozilgan.")
        
#     def remove_fan(self,fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#             return (f"{fan.nom} fani ro'yxatdan o'chirildi.")
#         else:
#             return ("Siz bu fanga yozilmagansiz.")
            
# matematika = Fan("Matematika")
# fizika = Fan("Fizika")

# talaba = Talaba("Shoxrux","Vohidov")
# print(talaba.fanga_yozil(fizika))
# print(talaba.fanga_yozil(matematika))
# print(talaba.fanga_yozil(matematika))

# print(talaba.remove_fan(fizika))        
# print(talaba.remove_fan(fizika))  

# class Shaxs:
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         info = f"{self.ism} {self.familiya}"
#         info += f"Passport {self.passport}, {self.tyil}-yilda tug'ilgan"
#         return info

#     def get_age(self,yil):
#         return yil-self.tyil

# class User(Shaxs):
#     def __init__(self,ism,familiya,username,email,phone_number):
#         super().__init__(ism=ism,familiya=familiya,passport=None,tyil=None)
#         self.username = username
#         self.email = email
#         self.phone_number = phone_number
    
#     def get_info(self):
#         info = f"Username:{self.username}\nName:{self.ism}\nEmail:{self.email}\nPhone number:{self.phone_number} "
#         return info

# # user = User(ism="Shoxrux",familiya="Vohidov",username="Karl",email="vohidovmillatumidvori01@gmail.com",phone_number=932142805)
# # print(user.get_info())

# class Admin(User):
#     def __init__(self,ism,familiya,username,email,phone_number):
#         super().__init__(ism,familiya,username,email,phone_number)
#         self.users = []
#         self.ban_users = []

#     def add_user(self,user):
#         if user not in self.users:
#             self.users.append(user)
#             return f"{user.ism} nomli foydalanuvchi qo'shildi!"
#         else:
#             return f"{user.ism} nomli user allaqachon mavjud"
    
#     def ban_user(self,user):
#         if user in self.users:
#             self.users.remove(user)
#             self.ban_users.append(user)
#             return f"{user.ism} foydalanuvchi bloklandi"
#         else:
#             return f"{user.ism} nomdagi foydalanuvchi hali mavjud emas"


# user1 = User("Ali", "Azizov", "Ali123", "ali@example.com", 998123456789)
# admin = Admin("Shoxrux", "Vohidov", "Karl", "vohidovmillatumidvori01@gmail.com", 932142805)

# # Foydalanuvchini qo'shamiz
# print(admin.add_user(user1))  # Ali nomli foydalanuvchi qo'shildi!

# # Foydalanuvchini bloklaymiz
# print(admin.ban_user(user1))  # Ali foydalanuvchi bloklandi
