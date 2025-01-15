# 07.01.2025
# vohidov
# listni tartiblash

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort() # katta harf kichik harifdan avval keladi
# print(cars)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
# print(sorted(mehmonlar))
# print(sorted(mehmonlar, reverse=True))

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)

# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)

# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits))

# sonlar = list(range(0,10))
# print(sonlar)

# juft_sonlar = list(range(0,10,2))
# toq_sonlar = list(range(1,10,2))
# print("juft sonlar:",juft_sonlar)
# print("toq sonlar:",toq_sonlar)

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[2:5]
# # my_cars[0] = 'matiz'
# print(my_cars)
# print(cars)

# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar[:] # nusxalash
# sonlar2.append(6)
# sonlar2.append(7)
# print(sonlar)
# print(sonlar2)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0:2])
# print(toys[-1])
# print(toys[2:5])
# toys[3] = 'dragon' # xato 

# amaliyot

# countries = ['uzbekistan','amerika','xitoy','rassiya','turkiya']
# print(sorted(countries))
# print(sorted(countries,reverse=True))
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# sonlar = list(range(120,1200,2))
# print(sonlar)
# print(sum(sonlar))
# eng_kichik = min(sonlar)
# eng_katta = max(sonlar)
# print(eng_katta-eng_kichik)
# print(len(sonlar))
# print(20,540-20,540//2)
# a = sonlar[0:20]
# b = sonlar[260:281]
# c =sonlar[520:]
# print(f"{a}\n{b}\n{c}")

# taomlar = ["mastava","palov","norin","moashxo'rda","lagmon"]
# nonushta = taomlar[:]
# nonushta.remove("lagmon")
# del nonushta[1]
# nonushta.append("olma")
# nonushta.insert(0,"novvot")
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# # nonushta[0] = "qaymoq va non"
# print(type(nonushta))