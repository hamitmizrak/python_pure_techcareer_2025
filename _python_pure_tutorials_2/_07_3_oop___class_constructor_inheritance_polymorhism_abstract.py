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
from abc import ABC, abstractmethod

# Abstract Class (Soyut Sınıf)
class Araba(ABC):  # ABC (Abstract Base Class) kullanılarak tanımlanır.
    def __init__(self, marka, model, yil, renk):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk

    @abstractmethod
    def calistir(self):
        """
        Soyut method: Bu method her alt sınıfta uygulanmak zorundadır.
        """
        pass

    def durdur(self):
        """
        Somut (Concrete) method: Alt sınıflar bu methodu olduğu gibi kullanabilir.
        """
        print(f"{self.marka} {self.model} durduruldu.")


########################################################################################
########################################################################################
# Alt Sınıf (Kalıtım ile Özelleştirme)
# Şimdi Araba sınıfından türeyen alt sınıflar oluşturacağız.
# Bu alt sınıflar, özel özellikler ve davranışlar ekleyerek ana sınıfı genişletebilir.
# OtomatikAraba Sınıfı
# Bu sınıf, otomatik şanzımanlı arabaları temsil eder.

# Alt Sınıf: OtomatikAraba
# OtomatikAraba (Abstract Class'tan türetilmiş bir sınıf)
class OtomatikAraba(Araba):
    def __init__(self, marka, model, yil, renk, vites_tipi="Otomatik"):
        super().__init__(marka, model, yil, renk)
        self.vites_tipi = vites_tipi

    # Abstract methodu implement etme (uygulama)
    def calistir(self):
        print(f"{self.marka} {self.model} otomatik modda çalıştırıldı.")

    def park_modu(self):
        print(f"{self.marka} {self.model} park moduna alındı.")

########################################################################################
########################################################################################
# ElektrikliAraba Sınıfı
# Bu sınıf, elektrikli arabaları temsil eder.
# Alt Sınıf: ElektrikliAraba
# ElektrikliAraba (Abstract Class'tan türetilmiş bir sınıf)
class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, renk, batarya_kapasitesi):
        super().__init__(marka, model, yil, renk)
        self.batarya_kapasitesi = batarya_kapasitesi

    # Abstract methodu implement etme (uygulama)
    def calistir(self):
        print(f"{self.marka} {self.model} elektrik modunda çalıştırıldı.")

    def sarj_et(self):
        print(f"{self.marka} {self.model} şarj ediliyor. Batarya kapasitesi: {self.batarya_kapasitesi} kWh.")


########################################################################################
########################################################################################

# Polymorphism Demonstrasyonu
def araba_calistir(temp):
    temp.calistir()

# Nesne Türetilmesi
otomatik_araba = OtomatikAraba("Audi", "A3", 2022, "Siyah")
elektrikli_araba = ElektrikliAraba("Tesla", "Model S", 2023, "Beyaz", 100)

# Polymorphic Kullanım
print("Polymorphism Örneği:")
araba_calistir(otomatik_araba)  # Çıktı: Audi A3 otomatik modda çalıştırıldı.
araba_calistir(elektrikli_araba)  # Çıktı: Tesla Model S elektrik modunda çalıştırıldı.

# Alt sınıflara özgü methodların kullanımı
otomatik_araba.park_modu()  # Çıktı: Audi A3 park moduna alındı.
elektrikli_araba.sarj_et()  # Çıktı: Tesla Model S şarj ediliyor. Batarya kapasitesi: 100 kWh.

################################################################################################
# ################################################################################################
# Açıklamalar
# Method Overriding (Geçersiz Kılma):

# Her iki alt sınıf (OtomatikAraba, ElektrikliAraba), üst sınıftaki calistir() methodunu geçersiz kılmıştır.
# Bu, her alt sınıfın kendi calistir() davranışını sergilemesini sağlar.
# Polymorphic Function (Çok Biçimli Fonksiyon):

# araba_calistir fonksiyonu, Araba sınıfı ve onun türevlerini parametre olarak alır.
# Parametre olarak aldığı nesnenin türüne bağlı olarak doğru calistir() methodunu çağırır.
# Alt Sınıfların Kendi Methodları:

# OtomatikAraba sınıfı için park_modu methodu.
# ElektrikliAraba sınıfı için sarj_et methodu, alt sınıflara özgü davranışları temsil eder.
# Bu yapı sayesinde, Araba türünden nesneler için ortak bir arabirim kullanılırken,
# alt sınıflar kendi özel davranışlarını sergileyebilir.
# Bu da polymorphism'in temel avantajını sağlar.

# Abstract İle İlgili Bilgiler
# Detaylı Açıklamalar
# 1. Abstract Class Nedir ve Neden Kullanılır?
# Tanım: Soyut sınıflar, kendisinden türetilen alt sınıfların belirli methodları mutlaka tanımlamasını zorunlu kılar.
# Bu, bir tür şablon görevi görür.
# Amaç:
# Ortak davranışları bir yerde toplamak.
# Alt sınıfların belirli kurallara uymasını sağlamak.
# Polymorphism ile bir arada kullanıldığında esnek ve yeniden kullanılabilir kod yapıları oluşturmak.

# 2. abc Modülü
# ABC (Abstract Base Class): Soyut sınıf oluşturmak için kullanılır.
# @abstractmethod: Alt sınıflarda uygulanması zorunlu methodları tanımlar.

# 3. Araba Sınıfı (Soyut Sınıf)
# Somut Method:
# durdur() yöntemi soyut değil, bu nedenle olduğu gibi alt sınıflar tarafından kullanılabilir.
# Soyut Method:
# @abstractmethod ile işaretlenmiş calistir() methodu alt sınıflar tarafından uygulanmak zorundadır.

# 4. Alt Sınıflar
# OtomatikAraba ve ElektrikliAraba:
# Bu sınıflar Araba sınıfını genişletir.
# Araba sınıfındaki calistir() methodunu implement (uygulamak) zorundadır. Eğer implement etmezsek, hata alırız.
# Ek olarak, bu sınıflar kendilerine özgü park_modu() ve sarj_et() gibi methodlar tanımlayabilir.
