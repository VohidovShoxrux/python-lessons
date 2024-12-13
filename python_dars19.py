# 13.12.2024
# vohidov
# MOSLASHUVCHAN FUNKSIYA *args **kwards keywords

# def oraliq(min, max):
#     sonalr = []
#     while min<max:
#         sonalr.append(min)
#         min += 1
#     return sonalr

# print(oraliq(0,10))

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)

# print(summa(1,2,3))

# def summa(*sonalr):
#     return sonalr

# a = summa(1,2,3,4,5,'olti')

# print(type(a))

# def avto_info(kampaniya, madel,**malumotlar):
#     """Avtomabillar haqida habar beruvchi"""
#     malumotlar['kampaniya']=kampaniya
#     malumotlar['model']=madel
#     return malumotlar

# avto1 = avto_info('GM','Malibu', rangi='qizil',yil=2020,karobka='avtmoat')

# print(avto1)

# Amaliyot

# def kopaytma(*sonlar):
#     yigindi = 1
#     for son in sonlar:
#         yigindi *= son
#     return yigindi
    
# print(summa(1,2,3,4),kopaytma(1,2,3,4))

# def talaba_info(ism,familiya,**malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familiya'] = familiya
#     return malumotlar

# talaba1 = talaba_info('shoxrux','vohidov',guruh=781,kurs=2,talim_shakli='sirtqi')
# print(talaba1)
