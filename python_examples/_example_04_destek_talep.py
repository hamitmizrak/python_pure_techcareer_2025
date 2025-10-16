"""
Gerçek Hayat Problemi: Müşteri Hizmetlerinde Destek Taleplerinin Analizi
Senaryo: Bir müşteri hizmetleri departmanında, gelen destek taleplerini analiz etmek ve yanıt sürelerini iyileştirmek istiyorsunuz.
Taleplerin türünü, sık kullanılan kelimeleri, en çok şikayet edilen konuları ve müşteri memnuniyetine dair ipuçlarını analiz ederek rapor oluşturabilirsiniz.
"""


# Örnek destek talepleri
destek_talepleri = [
    {
        "talep_no": 1,
        "kullanici": "ali123",
        "konu": "Fatura Problemi",
        "icerik": "Son faturamın tutarı beklediğimden fazla. Lütfen kontrol eder misiniz?",
        "kategori": "Fatura",
        "durum": "Çözüldü",
    },
    {
        "talep_no": 2,
        "kullanici": "ayse456",
        "konu": "Kargo Gecikmesi",
        "icerik": "Siparişim belirtilen teslimat tarihinde gelmedi. Acil çözüm rica ediyorum.",
        "kategori": "Kargo",
        "durum": "Beklemede",
    },
    {
        "talep_no": 3,
        "kullanici": "mehmet789",
        "konu": "Ürün İadesi",
        "icerik": "Yanlış ürün gönderildi. İade talep ediyorum.",
        "kategori": "İade",
        "durum": "Çözüldü",
    },
    {
        "talep_no": 4,
        "kullanici": "fatma321",
        "konu": "Teknik Destek",
        "icerik": "Ürünüm çalışmıyor. Teknik destek talep ediyorum.",
        "kategori": "Teknik Destek",
        "durum": "Beklemede",
    },
    {
        "talep_no": 5,
        "kullanici": "zeynep654",
        "konu": "Kargo Gecikmesi",
        "icerik": "Siparişim hâlâ teslim edilmedi. Lütfen bilgi verir misiniz?",
        "kategori": "Kargo",
        "durum": "Çözüldü",
    },
]

"""
Kodun Özellikleri
Talep Analizi: Toplam talep sayısı, kategori bazında dağılımı ve çözülme durumlarını analiz eder.
Kelime Frekansı: Destek taleplerinde sık kullanılan kelimeleri analiz ederek ortak sorunları tespit eder.
Kullanıcı Bazlı Analiz: Kullanıcıların oluşturduğu talep sayılarını gösterir.
Olumlu Geri Bildirim Oranı: Çözülmüş taleplerin oranını hesaplar.
Detaylı Listeleme: Çözülmemiş talepleri detaylı olarak listeler.

"""
# 1. Toplam destek talebi sayısı
# 2. Kategorilere göre talep sayısı
# 3. Çözülme durumuna göre talepler
# 4. Belirli bir kelimenin içeriklerde geçiş sıklığı
# 5. Taleplerin uzunluklarına göre sıralanması
# 6. En sık kullanılan kelimeler
# 7. Kullanıcı başına talep sayısı
# 8. Olumlu geri bildirimlerin oranı
# 9. Çözülmemiş taleplerin detayları


# 1. Toplam destek talebi sayısı
toplam_talep = len(destek_talepleri)
print(f"Toplam destek talebi sayısı: {toplam_talep}")

# 2. Kategorilere göre talep sayısı
print("\nKategorilere göre talep sayısı:")
kategori_talepleri = {}
for talep in destek_talepleri:
    kategori = talep["kategori"]
    kategori_talepleri[kategori] = kategori_talepleri.get(kategori, 0) + 1

for kategori, sayi in kategori_talepleri.items():
    print(f"{kategori}: {sayi} talep")

# 3. Çözülme durumuna göre talepler
print("\nÇözülme durumuna göre talepler:")
durum_talepleri = {"Çözüldü": 0, "Beklemede": 0}
for talep in destek_talepleri:
    durum = talep["durum"]
    durum_talepleri[durum] += 1

for durum, sayi in durum_talepleri.items():
    print(f"{durum}: {sayi} talep")

# 4. Belirli bir kelimenin içeriklerde geçiş sıklığı
aranan_kelime = "kargo"
gecis_sayisi = sum(1 for talep in destek_talepleri if aranan_kelime.lower() in talep["icerik"].lower())
print(f"\n'{aranan_kelime}' kelimesi {gecis_sayisi} içerikte geçiyor.")

# 5. Taleplerin uzunluklarına göre sıralanması
print("\nTalepler uzunluklarına göre sıralandı:")
destek_talepleri.sort(key=lambda x: len(x["icerik"]))
for talep in destek_talepleri:
    print(f"Talep No: {talep['talep_no']} - {talep['konu']} ({len(talep['icerik'])} karakter)")

# 6. En sık kullanılan kelimeler
print("\nDestek taleplerinde en sık kullanılan kelimeler:")
from collections import Counter

tum_kelimeler = []
for talep in destek_talepleri:
    kelimeler = talep["icerik"].lower().split()
    tum_kelimeler.extend(kelimeler)

kelime_sayilari = Counter(tum_kelimeler)
en_sik_kelimeler = kelime_sayilari.most_common(5)
for kelime, sayi in en_sik_kelimeler:
    print(f"{kelime}: {sayi} kez")

# 7. Kullanıcı başına talep sayısı
print("\nKullanıcı başına talep sayısı:")
kullanici_talepleri = {}
for talep in destek_talepleri:
    kullanici = talep["kullanici"]
    kullanici_talepleri[kullanici] = kullanici_talepleri.get(kullanici, 0) + 1

for kullanici, sayi in kullanici_talepleri.items():
    print(f"{kullanici}: {sayi} talep")

# 8. Olumlu geri bildirimlerin oranı
print("\nÇözülmüş taleplerin oranı:")
cozulmus_talepler = durum_talepleri["Çözüldü"]
oran = (cozulmus_talepler / toplam_talep) * 100
print(f"Çözülmüş taleplerin oranı: %{oran:.2f}")

# 9. Çözülmemiş taleplerin detayları
print("\nÇözülmemiş talepler:")
cozulmemis_talepler = [talep for talep in destek_talepleri if talep["durum"] == "Beklemede"]
for talep in cozulmemis_talepler:
    print(f"Talep No: {talep['talep_no']} - {talep['konu']} ({talep['icerik']})")
