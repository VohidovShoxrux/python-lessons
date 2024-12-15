# 13.12.2024
# vohidov
# FUNKSIYALAR. lambda

# import math

# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))

# kavadrat = lambda x, y : x**y
# print(kavadrat(3,2))

# def daraja(n):
#     return lambda x : x**n

# kavadrat = daraja(2)
# kub = daraja(3)
# num = kavadrat(5)
# print(num)
# print(f"3-ning kavadrati {kavadrat(3)} ga,"
#       f"kubi {kub(3)} ga teng")

# from math import sqrt # sqrt - kavadrat ildiz

# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# ildizlar = []
# for son in sonlar:
#     ildizlar.append(sqrt(son))

# def daraja2(x):
#     return x*x

# print(list(map(daraja2,sonlar))) 

# kavadratlar = list(map(lambda x:x*x,sonlar))
# print(kavadratlar)

# a = [3,1,6]
# b = [7,5,3]

# a_plus_b = list(map(lambda x,y : x+y,a,b))
# print(a_plus_b)

# import random as r

# sonlar = r.sample(range(100),10)
# print(sonlar)

# son = r.choice(range(10))
# print(son)

# def juftmi(x):
#     return x%2==0

# juft_sonlar = list(filter(juftmi,sonlar))
# juft_sonlar = list(filter(lambda x:x%2==0,sonlar))
# print(juft_sonlar)

# mevalar = ['olma','anor','shaftoli','gilos','banan']
# harf = 'b'
# mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)

# a = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')),mevalar))
# print(a)

