# 15.02.2025
# vohidov
# VORISLIK VA POLIMORFIZM

class Shaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info +=f" Passport:{self.passport}, {self.tyil}-yilida tug'ilgan"
        return info
    
    def get_age(self,yil):
        return yil-self.tyil

# inson = Shaxs("Hasan","Alimov","FB001122",1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")

class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil



class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    
    def get_id(self):
        return self.idraqam

    def get_bosqich(self):
        return self.bosqich

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

# talaba = Talaba("Shoxrux","Vohidov","FA112299",2005)
# print(talaba.get_info())

# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")

# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")

# print(f"{talaba.get_bosqich()}-bosqich talabasi")

# print(talaba.get_info())

talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)

print(talaba.manzil.get_manzil())

# print(talaba.manzil.get_info())

print(talaba.manzil.tuman)
