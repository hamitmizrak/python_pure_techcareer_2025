
### **Blockhain özellikleri **
1. **Okunabilir Zaman Damgası**  
   - Blokların zaman damgası artık **insan tarafından okunabilir bir tarih formatında** (`YYYY-MM-DD HH:MM:SS`) görüntüleniyor.

2. **Genesis (İlk) Bloğun Otomatik Oluşturulması**  
   - Blockchain başlatıldığında **ilk blok otomatik olarak oluşturuluyor** ve `previous_hash` değeri `"0"` olarak ayarlanıyor.

3. **İşlem Ekleme**  
   - Kullanıcılar **gönderen, alıcı ve miktar bilgileri ile işlem ekleyebilir**.

4. **Otomatik Madencilik**  
   - **3 işlem eklendiğinde** otomatik olarak madencilik işlemi başlatılıyor.

5. **Manuel Madencilik**  
   - Kullanıcı istediğinde `mine_block()` çağırarak **madencilik yapabilir ve yeni blok ekleyebilir**.

6. **Proof of Work Mekanizması**  
   - **Blokların hash değeri belirli sayıda sıfır ile başlamalı** (`difficulty` seviyesi kadar).
   - Bu, `nonce` değerini sürekli değiştirerek yeni hash hesaplamaları yaparak sağlanır.

7. **Blok Zincirinin Geçerliliğini Kontrol Etme**  
   - `is_chain_valid()` fonksiyonu ile **tüm blok zincirinin bütünlüğü doğrulanıyor**.
   - **Hash değerleri veya önceki blok hash değerleri bozulursa blockchain geçersiz olur.**

8. **Blockchain’i Konsola Yazdırma**  
   - `print_chain()` fonksiyonu **blokları ekrana daha okunaklı şekilde yazdırıyor**.
   - Her blok şu bilgileri içerir:
     - Blok Numarası
     - Zaman Damgası (Okunabilir)
     - Hash Değeri
     - Önceki Blok Hash Değeri
     - İşlemler

9. **Kullanıcı Bakiyesi Hesaplama**  
   - `get_balance(user)` fonksiyonu ile **belirli bir kullanıcının mevcut bakiyesi hesaplanıyor**.
   - Kullanıcının aldığı ve gönderdiği işlemler analiz edilerek toplam bakiye gösteriliyor.

10. **Blockchain Verisini JSON Formatında Dışa Aktarma**  
   - `export_to_json()` fonksiyonu **blockchain’i JSON formatına çevirerek dışa aktarıyor**.
   - JSON verisi terminalde görüntülenebilir veya bir dosyaya kaydedilebilir.

11. **Terminalde Renkli Çıktılar**  
   - `colorama` kütüphanesi kullanılarak **terminalde farklı renklerle bilgilendirme mesajları veriliyor**:
     - **Yeşil** → Başarıyla tamamlanan madencilik işlemleri.
     - **Kırmızı** → Hatalar veya eksik işlemler.
     - **Sarı** → Blockchain doğrulama durumu.
     - **Mavi** → Kullanıcı bakiyesi görüntüleme.
     - **Mor** → JSON formatındaki blockchain verisi.

