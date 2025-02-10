# 10.02.2025
# vohidov
# lambda

# import math 
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))

# product = lambda x, y : x**y
# print(product(3,2))

# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)

# print(f"4-ning kavadrati {kvadrat(4)} ga, kubi {kub(4)} ga teng")

# from math import sqrt

# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))

# def daraja2(x):
#     return x*x

# print(list(map(daraja2,sonlar)))

# kavadratlar = list(map(lambda x:x*x,sonlar))
# print(kavadratlar)

# kavadratlar = []

# for son in sonlar:
#     kavadratlar.append(son*son)

# print(kavadratlar)

# a = [ 2, 11, 53]
# b = [ 7, 31, 42]
# a_plus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)

# ismlar = ['shoxrux','samandar','abdulaziz','humoyun']
# print(list(map(lambda matn:matn.title(),ismlar)))

# import random as r

# sonlar = r.sample(range(100),10)

# def juftmi(x):
#     return x%2==0

# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random as r

# sonlar = r.sample(range(100),10)

# juft_sonlar = list(filter(lambda x:x%2==0,sonlar))

# print(sonlar)
# print(juft_sonlar)


# mevalar = ['olma','anjir','nok','gilos','uzum','limon','qovun','tarvuz','behi']

# mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva:len(meva)<=5,mevalar))
# print(mevalar2)

# mevalar3 = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))

# print(mevalar3)