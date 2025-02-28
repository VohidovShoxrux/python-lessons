def juft_sonlar(sonalr):
    return [son for son in sonalr if son % 2 == 0]
                
sonalr = list(range(1,10))
print(juft_sonlar(sonalr))