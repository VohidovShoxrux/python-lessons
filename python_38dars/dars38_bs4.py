# 05.03.2025
# vohidov
# BeautifulSoup4

import requests
from bs4 import BeautifulSoup

# url = "https://www.google.com"
# response = requests.get(url)
# html = response.text

# soup = BeautifulSoup(html, 'html.parser')

# havolalar = soup.find_all('a')

# for havola in havolalar:
#     if "google" in havola['href']:
#         print(havola.text)
#         print(havola['href'])
#         print("---")

# url = "https://weather.com/weather/today/l/41.30,69.27?par=google"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# harorat = soup.find('span', class_='CurrentConditions--tempValue--MHmYY')
# holat = soup.find('div', class_='CurrentConditions--phraseValue--mZC_p')

# if harorat and holat:
#     print(f"Toshkentdagi hozirgi harorat: {harorat.text}")
#     print(f"Ob-havo holati: {holat.text}")
# else:
#     print("Ma'lumot topilmadi, sayt tuzilishi o'zgargan bo'lishi mumkin.")

url = "https://kun.uz"
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Turli xil teg va klasslarni sinab ko'rish
    mumkin_bolgan_sarlavhalar = soup.find_all(['h1', 'h2', 'h3', 'a'], class_=['news-title', 'daily-news', 'title'])

    if mumkin_bolgan_sarlavhalar:
        for sarlavha in mumkin_bolgan_sarlavhalar:
            matn = sarlavha.text.strip()
            if matn:  # Bo'sh matnlarni o'tkazib yuborish
                print(matn)
                print("---")
    else:
        print("Hali ham sarlavhalar topilmadi. HTML tuzilishini qo'lda tekshirish kerak.")
        print("Sahifa boshlang'ich qismi:", soup.prettify()[:1000])  # Ko'proq ma'lumot uchun

except requests.exceptions.RequestException as e:
    print(f"Xatolik yuz berdi: {e}")