"""
Gerçek Hayatta String İşlemleri: Sosyal Medya Analizi ve Öneri Sistemi
Senaryo: Bir sosyal medya platformu yönettiğinizi düşünün.
Kullanıcılar içerik (paylaşım, yorum) oluşturuyor ve bu içeriklerin analiz edilmesi gerekiyor.
Aşağıda, Python kullanarak bu içerikler üzerinde string işlemleri yaparak bir analiz ve öneri sistemi geliştireceğiz.
Bu sistem, kullanıcı etkileşimlerini analiz edecek, metinleri işleyecek ve ilgi alanlarına göre öneriler sunacaktır.
"""


# Örnek sosyal medya içerikleri
icerikler = [
    {
        "kullanici": "ali123",
        "icerik": "Python programlama dili öğreniyorum. Çok keyifli!",
        "etiketler": ["#Python", "#Programlama", "#Eğitim"],
    },
    {
        "kullanici": "ayse456",
        "icerik": "Bugün spor salonunda harika bir antrenman yaptım! 💪",
        "etiketler": ["#Spor", "#Sağlık", "#Motivasyon"],
    },
    {
        "kullanici": "mehmet789",
        "icerik": "JavaScript ile web uygulamaları geliştirmek çok eğlenceli.",
        "etiketler": ["#JavaScript", "#WebGeliştirme", "#Kodlama"],
    },
    {
        "kullanici": "fatma321",
        "icerik": "Python ve veri analizi konularında yeni bilgiler öğreniyorum.",
        "etiketler": ["#Python", "#VeriAnalizi", "#Eğitim"],
    },
    {
        "kullanici": "zeynep654",
        "icerik": "Kahve eşliğinde kitap okumak en sevdiğim şey. ☕📚",
        "etiketler": ["#Kahve", "#Kitap", "#Huzur"],
    }
]

"""
Kodun Özellikleri
Toplam İçerik Sayısı: Platformdaki içeriklerin toplamını bulur.
Kullanıcı Analizi: Kullanıcı başına içerik sayısını hesaplar.
Kelime Analizi: Belirli bir kelimenin içeriklerde ne sıklıkla geçtiğini kontrol eder.
İçerik Özetleme: Uzun içerikleri kısaltır.
Etiket Analizi: En popüler etiketleri listeler.
Öneri Sistemi: Kullanıcıların ortak etiketlerine göre bağlantılar önerir.
Benzersiz Kelimeler: Tüm içeriklerde geçen kelimeleri analiz eder.
Filtreleme: Belirli bir kullanıcıya ait içerikleri filtreler.
"""
# 1. Toplam içerik sayısını bulma
# 2. Kullanıcı başına içerik sayısını hesaplama
# 3. Belirli bir kelimenin içeriklerde geçiş sıklığını bulma
# 4. İçerikleri uzunluklarına göre sıralama
# 5. En popüler etiketleri bulma
# 6. Kullanıcı öneri sistemi (ilgi alanlarına göre)
# Kullanıcı öneri sistemi: Aynı etiketi paylaşan kullanıcıları önerme
# 7. İçerik özetleri
# 8. Benzersiz kelimeleri bulma
# 9. Belirli bir kullanıcıya ait içerikleri filtreleme



# 1. Toplam içerik sayısını bulma
toplam_icerik = len(icerikler)
print(f"Toplam içerik sayısı: {toplam_icerik}")

# 2. Kullanıcı başına içerik sayısını hesaplama
kullanici_icerik_sayisi = {}
for icerik in icerikler:
    kullanici = icerik["kullanici"]
    kullanici_icerik_sayisi[kullanici] = kullanici_icerik_sayisi.get(kullanici, 0) + 1

print("\nKullanıcı başına içerik sayısı:")
for kullanici, sayi in kullanici_icerik_sayisi.items():
    print(f"{kullanici}: {sayi} içerik")

# 3. Belirli bir kelimenin içeriklerde geçiş sıklığını bulma
aranan_kelime = "Python"
gecis_sayisi = sum(1 for icerik in icerikler if aranan_kelime.lower() in icerik["icerik"].lower())
print(f"\n'{aranan_kelime}' kelimesi {gecis_sayisi} içerikte geçiyor.")

# 4. İçerikleri uzunluklarına göre sıralama
print("\nİçerikler uzunluklarına göre sıralandı:")
icerikler.sort(key=lambda x: len(x["icerik"]))
for icerik in icerikler:
    print(f"{icerik['icerik']} ({len(icerik['icerik'])} karakter)")

# 5. En popüler etiketleri bulma
from collections import Counter

tum_etiketler = [etiket for icerik in icerikler for etiket in icerik["etiketler"]]
etiket_sayilari = Counter(tum_etiketler)
en_populer_etiketler = etiket_sayilari.most_common(3)

print("\nEn popüler etiketler:")
for etiket, sayi in en_populer_etiketler:
    print(f"{etiket}: {sayi} kez kullanılmış")

# 6. Kullanıcı öneri sistemi (ilgi alanlarına göre)
kullanici_ilgi_alani = {}
for icerik in icerikler:
    kullanici = icerik["kullanici"]
    etiketler = icerik["etiketler"]
    kullanici_ilgi_alani[kullanici] = kullanici_ilgi_alani.get(kullanici, set()).union(etiketler)

print("\nKullanıcı ilgi alanları:")
for kullanici, ilgi_alanlari in kullanici_ilgi_alani.items():
    print(f"{kullanici}: {', '.join(ilgi_alanlari)}")

# Kullanıcı öneri sistemi: Aynı etiketi paylaşan kullanıcıları önerme
print("\nKullanıcı öneri sistemi:")
for kullanici, ilgi_alanlari in kullanici_ilgi_alani.items():
    print(f"{kullanici} için öneriler:")
    ortak_kullanicilar = [
        k
        for k, alanlar in kullanici_ilgi_alani.items()
        if k != kullanici and not ilgi_alanlari.isdisjoint(alanlar)
    ]
    print(f"  Önerilen kullanıcılar: {', '.join(ortak_kullanicilar)}" if ortak_kullanicilar else "  Öneri bulunamadı.")

# 7. İçerik özetleri
print("\nİçerik özetleri:")
for icerik in icerikler:
    orijinal = icerik["icerik"]
    ozet = orijinal[:50] + "..." if len(orijinal) > 50 else orijinal
    print(f"{icerik['kullanici']} içerik özeti: {ozet}")

# 8. Benzersiz kelimeleri bulma
print("\nTüm içeriklerde geçen benzersiz kelimeler:")
tum_kelimeler = set()
for icerik in icerikler:
    kelimeler = icerik["icerik"].split()
    tum_kelimeler.update(kelimeler)

print(f"Benzersiz kelimeler ({len(tum_kelimeler)} adet): {tum_kelimeler}")

# 9. Belirli bir kullanıcıya ait içerikleri filtreleme
kullanici_adi = "fatma321"
kullanici_icerikleri = [icerik for icerik in icerikler if icerik["kullanici"] == kullanici_adi]

print(f"\n{kullanici_adi} kullanıcısına ait içerikler:")
for icerik in kullanici_icerikleri:
    print(f"- {icerik['icerik']}")
