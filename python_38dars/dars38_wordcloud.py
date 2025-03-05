# 05.04.2025
# vohidov
# wordcloud va matplotlib

import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 

# Sahifadan ma'lumot olish
sahifa = "https://daryo.uz"
try:
    r = requests.get(sahifa)
    r.raise_for_status()  # Agar sahifa yuklanmasa xatolik chiqaradi
except requests.exceptions.RequestException as e:
    print(f"Xatolik: Sahifani yuklab bo‘lmadi. Sabab: {e}")
    exit()

soup = BeautifulSoup(r.text, 'html.parser')
# "daryo.uz" saytida sarlavhalar odatda "h2" tegi yoki maxsus klass bilan keladi
news = soup.find_all("h2")  # Sarlavhalar "h2" tegi ichida bo‘lishi mumkin
matn = ""
for n in news:
    matn += n.text.strip() + " "  # Har bir sarlavha orasiga bo‘shliq qo‘shdim

# Matnni tekshirish
print("Matn:", matn)
print("Matn uzunligi:", len(matn))

# Kerakmas so‘zlar
stopwords = ["учун", "бўйича", "лекин", "билан", "ва", "бор", "ҳам", "хил", "йил"]

# Agar matn bo‘sh bo‘lmasa, so‘z bulutini yaratish
if not matn or matn.strip() == "":
    print("Xatolik: Sahifadan matn olinmadi yoki matn bo‘sh.")
else:
    wordcloud = WordCloud(width=1000, height=1000, 
                          background_color='white', 
                          stopwords=stopwords, 
                          min_font_size=20).generate(matn)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()