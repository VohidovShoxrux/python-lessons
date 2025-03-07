# 07.03.2025
# vohidov
# 1 dan 100 gacha sonlar ro'yxatidan qolib ketgan sonni topish 

import random
n=100
numbers = list(range(1,n+1))
x=numbers.pop(random.randint(1,n+1))
print(x)

# # 1-usul
# numbers2 = list(range(1,n+1))
# print(sum(numbers2)-sum(numbers))

# 2-usul
# for i in range(1,n):
#     if i not in numbers:
#         print(i)
#         break

# 3-usul

# summa = n*(n+1)/2
# print(summa-sum(numbers))