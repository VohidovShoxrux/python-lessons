# 23.10.2024
# vohidov 
# Lists

# cars = ["bmw", "huyunday", "mersedes", "astonmartin", "chaqmoqmakvin"]
# cars.sort()
# print(cars)
# cars.append("Rolsroys")
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# # print(cars)
# print(sorted(cars))
# print(sorted(cars, reverse=True))

# sonlar = [ 8, 3, 1, 9, 4, 7, 2, 6, 0, 5]
# print(sorted(sonlar))
# print(sorted(sonlar, reverse=True))
# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True)
# # print(sonlar)

# cars.reverse()
# print(cars)
# uzunlik = len(cars)
# print(uzunlik)
# nubers = list(range(0,10))
# print(nubers)
# toq_sonlar = list(range(1,11,2))
# print(toq_sonlar)
# juft_sonlar = list(range(2,11,2))
# print(juft_sonlar)
# narhlar = [4700, 2500, 55000, 129000, 30000, 7000]
# print("Minimum narx", min(narhlar), "so\'m")
# print("Maxsimum narx", max(narhlar), "so\'m")
# print("Umumiy miqdori", sum(narhlar), "so\'m")

# friends = ["Zubayir", "Fuzayil", "Zahro", "Saddam", "Marziya", "Hamza"]
# print(friends[1:2])
# print(friends[:-1])
# print(friends[1:])
# print(friends[0:])
# print(friends)

# my_friends = friends
# print(my_friends)
# print(friends)
# my_friends.remove("Fuzayil")
# my_friends[-1] = "Hakima"
# print(my_friends)
# print(friends)

# friends = ["Zubayir", "Fuzayil", "Zahro", "Saddam", "Marziya", "Hamza"]
# my_friends = friends[:]
# my_friends.remove("Fuzayil")
# my_friends.append("Asadbek")
# print(my_friends)
# print(friends)

# TUPLE o'zgarmas ro'yxat tuzish
# toys = ("car", 'bus', 'bear', 'rabbit', 'turtle')
# print(toys[:])
# print(toys[0])
# print(toys[2:3])
# print(toys[-1])
# toys[-1] = "teddy"
# print(toys)
# toys = list(toys)
# toys.append("teddy")
# print(toys,type(toys))
# toys = tuple(toys)
# print(type(toys))

# AMALIYOT
# countries = ["O'zbekiston", "Angilya", "Rassiya", "Amerika", "Polsha", "Korea", "Xitoy", "Fransiya", "Ispaniya"]
# print(len(countries))
# print(sorted(countries))
# print(sorted(countries, reverse=True))
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# juft_sonlar = list(range(120, 1200,2))
# print(juft_sonlar)
# min_son = min(juft_sonlar)
# max_son = max(juft_sonlar)
# jami_sonlar = sum(juft_sonlar)
# print("Eng kichik son ushbuga teng: ", min_son, "\nEng katta son ushbuga teng: ", max_son, "\nJami sonlar yig'indisi ushbuga teng: ",jami_sonlar)
# elementlar_soni = len(juft_sonlar)
# print("elementlar soni: ",elementlar_soni)
# print("boshidan:",juft_sonlar[0:21],"\no'rtasidan:",juft_sonlar[260:281],"\noxiridan:",juft_sonlar[520:])
# meals = ["soup", "pasta", "fish", "Sushi", "Burger"]
# breakfast = meals[:]
# breakfast.remove("soup")
# breakfast.remove("pasta")
# breakfast.append("salad")
# breakfast.append("pizza")
# print(meals)
# print(breakfast)
# breakfast = tuple(breakfast)
# # breakfast[0] = "qaymoq va non"
# print(breakfast)