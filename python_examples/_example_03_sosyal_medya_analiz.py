
"""
Gerçek Hayatta String İşlemleri: Sosyal Medya Analizi ve Öneri Sistemi
Senaryo: Bir sosyal medya platformu yönettiğinizi düşünün.

Kullanıcılar içerik (paylaşım, yorum) oluşturuyor ve bu içeriklerin analiz edilmesi gerekiyor.
Aşağıda, Python kullanarak bu içerikler üzerinde string işlemleri yaparak bir analiz ve öneri sistemi geliştireceğiz.
Bu sistem, kullanıcı etkileşimlerini analiz edecek, metinleri işleyecek ve ilgi alanlarına göre öneriler sunacaktır.
"""

# Örnek ürün yorumları
yorumlar = [
    {
        "kullanici": "ali123",
        "urun": "Kablosuz Kulaklık",
        "puan": 5,
        "yorum": "Harika bir ürün! Ses kalitesi çok iyi ve kullanımı kolay.",
    },
    {
        "kullanici": "ayse456",
        "urun": "Kablosuz Kulaklık",
        "puan": 4,
        "yorum": "Fiyatına göre oldukça iyi. Ancak pil ömrü biraz daha uzun olabilirdi.",
    },
    {
        "kullanici": "mehmet789",
        "urun": "Dizüstü Bilgisayar",
        "puan": 3,
        "yorum": "Performansı idare eder. Ancak ekran kalitesi beklediğim gibi değil.",
    },
    {
        "kullanici": "fatma321",
        "urun": "Dizüstü Bilgisayar",
        "puan": 1,
        "yorum": "Hayal kırıklığı! Ürün çok yavaş ve batarya süresi çok kötü.",
    },
    {
        "kullanici": "zeynep654",
        "urun": "Akıllı Saat",
        "puan": 5,
        "yorum": "Çok şık bir tasarım. Tüm özellikleri kusursuz çalışıyor!",
    },
    {
        "kullanici": "can789",
        "urun": "Kablosuz Kulaklık",
        "puan": 2,
        "yorum": "Ses kalitesi kötü ve bağlantı sorunları yaşıyorum.",
    },
]

"""
Kodun Özellikleri
Yorum Analizi: Toplam yorum sayısı, ürün bazında yorum sayıları ve puanları analiz edilir.
Olumlu/Olumsuz Yorumlar: Yorumlar puana göre sınıflandırılır.
Popülerlik Belirleme: En çok yorum alan ürün tespit edilir.
Kelime Analizi: Belirli kelimelerin geçiş sıklığı ve benzersiz kelimeler bulunur.
Yorum Özetleme: Uzun yorumlar kısaltılarak özetler sunulur.
Bu örnek, gerçek hayatta e-ticaret platformlarında ürün yorumlarının nasıl analiz edilebileceğini kapsamlı bir şekilde göstermektedir.
"""
# 1. Toplam yorum sayısı
# 2. Ürünlere göre yorum sayısı
# 3. Ortalama puan hesaplama
# 4. Olumsuz yorumları bulma (Puan 3 ve altında olanlar)
# 5. Belirli bir kelimenin yorumlarda geçme sıklığı
# 6. Yorumları uzunluklarına göre sıralama
# 7. En popüler ürünü belirleme
# 8. Kullanıcı başına ortalama puan hesaplama
# 9. Olumlu yorumları özetleme (Puan 4 ve üzeri olanlar)
# 10. Benzersiz kelimeleri bulma


# 1. Toplam yorum sayısı
toplam_yorum = len(yorumlar)
print(f"Toplam yorum sayısı: {toplam_yorum}")

# 2. Ürünlere göre yorum sayısı
print("\nÜrünlere göre yorum sayısı:")
urun_yorum_sayisi = {}
for yorum in yorumlar:
    urun = yorum["urun"]
    urun_yorum_sayisi[urun] = urun_yorum_sayisi.get(urun, 0) + 1

for urun, sayi in urun_yorum_sayisi.items():
    print(f"{urun}: {sayi} yorum")

# 3. Ortalama puan hesaplama
print("\nÜrünlere göre ortalama puanlar:")
urun_puanlari = {}
for yorum in yorumlar:
    urun = yorum["urun"]
    puan = yorum["puan"]
    if urun not in urun_puanlari:
        urun_puanlari[urun] = []
    urun_puanlari[urun].append(puan)

for urun, puanlar in urun_puanlari.items():
    ortalama_puan = sum(puanlar) / len(puanlar)
    print(f"{urun}: {ortalama_puan:.2f} puan")

# 4. Olumsuz yorumları bulma (Puan 3 ve altında olanlar)
print("\nOlumsuz yorumlar:")
olumsuz_yorumlar = [yorum for yorum in yorumlar if yorum["puan"] <= 3]
for yorum in olumsuz_yorumlar:
    print(f"{yorum['urun']} - {yorum['kullanici']}: {yorum['yorum']} (Puan: {yorum['puan']})")

# 5. Belirli bir kelimenin yorumlarda geçme sıklığı
aranan_kelime = "ses"
gecis_sayisi = sum(1 for yorum in yorumlar if aranan_kelime.lower() in yorum["yorum"].lower())
print(f"\n'{aranan_kelime}' kelimesi {gecis_sayisi} yorumda geçiyor.")

# 6. Yorumları uzunluklarına göre sıralama
print("\nYorumlar uzunluklarına göre sıralandı:")
yorumlar.sort(key=lambda x: len(x["yorum"]))
for yorum in yorumlar:
    print(f"{yorum['urun']} - {yorum['yorum']} ({len(yorum['yorum'])} karakter)")

# 7. En popüler ürünü belirleme
print("\nEn popüler ürünü belirleme:")
en_populer_urun = max(urun_yorum_sayisi, key=urun_yorum_sayisi.get)
print(f"En popüler ürün: {en_populer_urun} ({urun_yorum_sayisi[en_populer_urun]} yorum)")

# 8. Kullanıcı başına ortalama puan hesaplama
print("\nKullanıcı başına ortalama puanlar:")
kullanici_puanlari = {}
for yorum in yorumlar:
    kullanici = yorum["kullanici"]
    puan = yorum["puan"]
    if kullanici not in kullanici_puanlari:
        kullanici_puanlari[kullanici] = []
    kullanici_puanlari[kullanici].append(puan)

for kullanici, puanlar in kullanici_puanlari.items():
    ortalama_puan = sum(puanlar) / len(puanlar)
    print(f"{kullanici}: {ortalama_puan:.2f} puan")

# 9. Olumlu yorumları özetleme (Puan 4 ve üzeri olanlar)
print("\nOlumlu yorumlar (özet):")
olumlu_yorumlar = [yorum for yorum in yorumlar if yorum["puan"] >= 4]
for yorum in olumlu_yorumlar:
    orijinal = yorum["yorum"]
    ozet = orijinal[:50] + "..." if len(orijinal) > 50 else orijinal
    print(f"{yorum['urun']} - {yorum['kullanici']}: {ozet}")

# 10. Benzersiz kelimeleri bulma
print("\nTüm yorumlarda geçen benzersiz kelimeler:")
tum_kelimeler = set()
for yorum in yorumlar:
    kelimeler = yorum["yorum"].split()
    tum_kelimeler.update(kelimeler)

print(f"Benzersiz kelimeler ({len(tum_kelimeler)} adet): {tum_kelimeler}")
