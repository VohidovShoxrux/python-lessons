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
    
    def __len__(self):
        return len(self.avtolar)

    def __getitem__(self,index):
        return self.avtolar[index]

    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
    
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            elif isinstance(qiymat.Avto):
                self.add_avto(qiymat)
            else:
                print(f"AvtoSalon ga {type(qiymat)} qo'shib bo'lmaydi")
    
    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name}  {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
    
    def __call__(self, *param):
        if param:
            for avto in  param:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]

salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)

salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)

salon3 = salon1 + salon2
# print(salon3)
# print(salon3[:])

avto7 = Avto("BMW", 'X7','Qora',2015,75000)
salon1 + avto7
print(salon1())

avto_new = Avto("Mercedes-Benz", 'E200','Silver',2015,80000)
salon1(avto_new) # Yangi avto qo'shamiz
salon1() # salondagi mashinalarni ko'ramiz