# public
# private : Encapsulation GET,SET

# Python'da yapıcı metot: __init__ bu metot
# __init__: Bir sınıf örneğimizi oluşturduğumuzda __init__ olan metot otomatik çağrılır.
# Self Parametresi: Python'da bir metot içinde olan o anki nesneye erişmek için kullanılır.

# Python'da yapıcı metot: __init__ bu metot
# __init__: Bir sınıf örneğimizi oluşturduğumuzda __init__ olan metot otomatik çağrılır.
# Self Parametresi: Python'da bir metot içinde olan o anki nesneye erişmek için kullanılır.

# Access Modifier(Erişim belirleyiciler)
# public, private, protected

# Public (Genel Erişim)
"""
Bir değişkene veya Metototlara doğrudan erişim
isimlendirmek için özel bir işaretimiz yoktur
Örnek: self.marka
"""
from datetime import datetime

# Protected (Özel Erişim)
"""
protected data _ (tek alt çizgi)
Bir değişkene veya Metototlara encapulatin GETTER, AND SETTER ile erişim
isimlendirmek için özel bir işaretimiz 1 tane alt çizgi
Örnek: self.__marka
"""

# Private (Özel Erişim)
"""
private data __ (iki tane alt çizgi)
Bir değişkene veya Metototlara encapulatin GETTER, AND SETTER ile erişim
isimlendirmek için özel bir işaretimiz 2 tane alt çizgi
Örnek: self.__marka
"""

# Tür Güvenliği (Type Hints)
# Python >=3.5 sonrasında type hint özelliğimizi değişkene veya fonksiyonlara ekleyebiliriz.

class Araba:

    # CONSTRUCTOR
    def __init__(self,
                 marka: str = "Bilinmiyor",
                 modeling: str = "Bilinmiyor",
                 yil: str = "1970-01-01",
                 renk: str = "Bilinmiyor") -> None:
        self.__marka  = marka      # private   access   (2 tane alt çizgi)
        self._modeling = modeling  # protected accses   ( 1 tane çizgi)
        self.yil     = yil         # public    access   (0 tane çizgi )
        self.renk    = renk        # public    access   (0 tane çizgi )
        print(f"Araba sınıfından yeni bir örnek oluşturuldu")

    # METHOD
    def goster_bilgileri(self) -> None:
        print(f"Marka: {self.__marka}, modeling: {self._modeling}, Yıl: {self.yil}, Renk: {self.renk}")

    # SETTER AND GETTER (VALIDATION)
    # Marka SET (private: Çift çizgi)
    def set_marka(self,marka:str) -> None:
        if not isinstance(marka,str):
            raise TypeError("Marka, string olmalıdır.")
        self.__marka = marka

    # Marka GET(private: Çift Çizgi)
    def get_marka(self) -> str:
        return self.__marka

    # modeling SET (protected: Tek çizgi)
    def set_modeling(self, modeling:str) -> None:
        if not isinstance(modeling, str):
            raise TypeError("Model, string olmalıdır.")
        self._modeling = modeling


    # modeling GET (protected: Tek çizgi)
    def get_modeling(self) -> str:
        return self._modeling

    # yil SET (public: 0 çizgi)
    def set_yil(self, yil:str) -> None:
        if not isinstance(yil, str):
            raise TypeError("Yıl, string olmalıdır. ve YYYY-MM-DD foramtında olmalıdır")
        try:
            self.yil = datetime.strptime(yil, '%Y-%m-%d')
        except ValueError:
            print(f"Geçersiz Tarih Formatında yazdınız. Lütfen YYYY-MM-DD şeklinde yazınız")

    # yil GET (public: 0 çizgi)
    def get_yil(self) -> str:
        return self.yil.strftime('%Y-%m-%d')

    # renk SET (public: 0 çizgi)
    def set_renk(self, renk:str) -> None:
        if not isinstance(renk, str):
            raise TypeError("Renk, string olmalıdır.")
        self.renk = renk

    # renk GET (public: 0 çizgi)
    def get_renk(self) -> str:
        return self.renk


################################################################################
print(f"#######################################################################")
araba1= Araba()
araba1.goster_bilgileri()


################################################################################
print(f"#######################################################################")
araba2= Araba()
araba2.set_marka("Audi")
araba2.set_modeling("A3")
araba2.set_yil("2020-01-01")
araba2.set_renk("Beyaz")
araba2.goster_bilgileri()


################################################################################
print(f"#######################################################################")
araba3= Araba()
#araba3.set_marka(1234)     # Error: Marka, string olmalıdır.
#araba3.set_modeling(1234)  # Error: Model, string olmalıdır.
araba3.set_yil("2020-13")  # Error: Geçersiz Tarih Formatında yazdınız. Lütfen YYYY-MM-DD şeklinde yazınız


