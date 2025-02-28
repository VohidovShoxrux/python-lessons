def uchson_katta(a,b,c):
    if a > b:
        if a>c:
            return a
        else:
            return c
    elif b > c:
        return b 
    else:
        return c

print(uchson_katta(8,4,5))