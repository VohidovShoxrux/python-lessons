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

class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
    
    def get_id(self):
        return self.idraqam

    def get_bosqich(self):
        return self.bosqich

# talaba = Talaba("Shoxrux","Vohidov","FA112299",2005)
# print(talaba.get_info())

talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")

# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")

print(f"{talaba.get_bosqich()}-bosqich talabasi")