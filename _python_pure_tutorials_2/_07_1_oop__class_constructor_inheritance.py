# Python'da kalıtım (inheritance),
# bir sınıfın (ana sınıf veya üst sınıf) özelliklerini ve metotlarını başka bir sınıfa (alt sınıf) devretmesini sağlar.
# Bu mekanizma, kodun yeniden kullanılabilirliğini artırır ve daha organize bir yapı oluşturmayı mümkün kılar.
# Araba sınıfını kullanarak kalıtımı açıklayalım.

# Kalıtım ile Çalışma Mantığı
# super() Metodu:

# Alt sınıflar, super() metodu ile üst sınıfın özelliklerini ve metotlarını kullanabilir.
# super().__init__() ifadesi, üst sınıfın yapıcı metodunu çağırır.
# Alt Sınıflar Yeni Özellikler Ekler:

# Alt sınıflar, üst sınıfın özelliklerini genişleterek (örneğin, vites_tipi ve batarya_kapasitesi) özel özellikler ekleyebilir.
# Kodun Yeniden Kullanılabilirliği:
# Aynı temel özelliklere sahip sınıflar türetmek için kod tekrarını önler.

# Kalıtımın Avantajları
# Kod Tekrarını Azaltır: Ortak özellik ve metotlar bir üst sınıfta tanımlanır ve alt sınıflarda tekrar yazılmadan kullanılır.
# Modülerlik ve Genişletilebilirlik Sağlar: Üst sınıf genişletilerek alt sınıflar oluşturulabilir.
# Hiyerarşik Yapı Sunar: Sınıflar arasında ilişki kurarak organize bir yapı sağlar.

# Sonuç
# Yukarıdaki örnekte, Araba sınıfı bir temel (üst) sınıf olarak kullanıldı ve OtomatikAraba ve ElektrikliAraba sınıfları,
# bu sınıftan türetildi. Böylece hem kod tekrarından kaçınılmış oldu
# hem de arabaların özelliklerine göre özelleştirilmiş davranışlar tanımlandı.
# Bu yapı, OOP'nin kalıtım prensibini gerçek hayatta uygulamak için güçlü bir araçtır.


# Araba Sınıfı (Üst Sınıf)
# Önce temel bir Araba sınıfı oluşturuyoruz. Bu sınıf, tüm arabaların ortak özelliklerini ve davranışlarını tanımlar.
class Araba:

    # Constructor
    def __init__(self, marka, model, yil, renk):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk

    # Function
    def calistir(self):
        print(f"{self.marka} {self.model} {self.renk} {self.yil} çalıştırıldı.")

    # Function
    def durdur(self):
        print(f"{self.marka} {self.model} durduruldu.")


########################################################################################
########################################################################################
# Alt Sınıf (Kalıtım ile Özelleştirme)
# Şimdi Araba sınıfından türeyen alt sınıflar oluşturacağız.
# Bu alt sınıflar, özel özellikler ve davranışlar ekleyerek ana sınıfı genişletebilir.
# OtomatikAraba Sınıfı
# Bu sınıf, otomatik şanzımanlı arabaları temsil eder.

# Alt Sınıf: OtomatikAraba
class OtomatikAraba(Araba):
    def __init__(self, marka, model, yil, renk, vites_tipi="Otomatik"):
        super().__init__(marka, model, yil, renk)
        self.vites_tipi = vites_tipi

    # calistir() methodunu geçersiz kılma (override)
    def calistir(self):
        print(f"{self.marka} {self.model} otomatik modda çalıştırıldı.")

    def park_modu(self):
        print(f"{self.marka} {self.model} park moduna alındı.")


########################################################################################
########################################################################################
# ElektrikliAraba Sınıfı
# Bu sınıf, elektrikli arabaları temsil eder.
# Alt Sınıf: ElektrikliAraba
class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, renk, batarya_kapasitesi):
        super().__init__(marka, model, yil, renk)
        self.batarya_kapasitesi = batarya_kapasitesi

    # calistir() methodunu geçersiz kılma (override)
    def calistir(self):
        print(f"{self.marka} {self.model} elektrik modunda çalıştırıldı.")

    def sarj_et(self):
        print(f"{self.marka} {self.model} şarj ediliyor. Batarya kapasitesi: {self.batarya_kapasitesi} kWh.")


########################################################################################
########################################################################################
# Otomatik Araba Nesnesi
otomatik_araba = OtomatikAraba("Audi", "A3", 2022, "Siyah")
otomatik_araba.calistir()  # Çıktı: Audi A3 Siyah 2022 çalıştırıldı.
otomatik_araba.park_modu()  # Çıktı: Audi A3 park moduna alındı.

# Elektrikli Araba Nesnesi
elektrikli_araba = ElektrikliAraba("Tesla", "Model S", 2023, "Beyaz", 100)
elektrikli_araba.calistir()  # Çıktı: Tesla Model S Beyaz 2023 çalıştırıldı.
elektrikli_araba.sarj_et()  # Çıktı: Tesla Model S şarj ediliyor. Batarya kapasitesi: 100 kWh.

