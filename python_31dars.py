# 18.10.2025
# vohidov
# DUNDER METODLAR

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    def __repr__(self):
        return f"Avto: {self.rang} {self.make} {self.model}"

    def __eq__(self,boshqa_avto):
        return self.narh == boshqa_avto.narh

    def __lt__(self,boshqa_avto):
        return self.narh<boshqa_avto.narh

    def __le__(self,boshqa_avto):
        return self.narh <= boshqa_avto.narh
    
# # avto1 = Avto("GM","Malibu","Qora",2020,40000)
# # print(avto1) # obyekt haqida ma'lumot

# # x,y = 5,10
# # print(x>y)

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,40000)
# print(avto1==avto2)

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def add_avto(self,avto):
        if isinstance(avto,Avto):
            pass

salon1 = AvtoSalon("MaxAvto")
print(salon1)