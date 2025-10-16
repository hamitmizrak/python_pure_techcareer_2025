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

# Log Yapılandırılması
"""
filename="araba_log.txt", : Nereye kayıt edilecek
level=logging.INFO : Logların ne düzeyde yazılacağı 
DEBUG : Hata ayıklamak
INFO : Bilgi
WARNING: Potansiyel bir sroun  teşkil edecek
ERROR : Hatalar
CRITICAL: Kritik hata(Sistem çöktü)
format='%(asctime)s - %(levelname)s - %(message)s' : Logların yazılacağı format
name= Logger adı
funcName= Log çağrısında yapılan fonskiyon adı
lineno = Log çağrısını yapıldığı satır numarası
"""
import logging  # Loglama
from datetime import datetime # Date
from enum import Enum
import os


# https://docs.python.org/3/library/logging.html
# Log yapılandırması
# Log dosyasının adını tanımla
log_dosya_adi = "araba_log.txt"
log_dosya_yolu = os.path.join(os.getcwd(), log_dosya_adi)

# Eğer dosya varsa yeni bir dosya oluştur
if os.path.exists(log_dosya_yolu):
    yeni_log_dosya_adi = f"araba_log_{len(os.listdir(os.getcwd()))}.txt"
    log_dosya_yolu = os.path.join(os.getcwd(), yeni_log_dosya_adi)
    print(f"Dosya mevcut. Yeni log dosyası oluşturuldu: {yeni_log_dosya_adi}")
else:
    print(f"Log dosyası bulunamadı. Yeni log dosyası oluşturulacak: {log_dosya_adi}")

# Logging yapılandırması
logging.basicConfig(
    filename=log_dosya_yolu,
    level=logging.INFO,
    format='%(asctime)s %(name)s: %(levelname)s: %(lineno)s = %(funcName)s ,  %(message)s , '
)

# üğşçö
# Enum(Renk)
class Renk(Enum):
    KIRMIZI = '\033[91m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    MAVI = '\033[94m'
    BEYAZ = '\033[97m'
    SIFIRLA = '\033[0m'

# Enum (Yakıt)
class YakitTuru(Enum):
    BENZIN ="Benzin",
    DIZEL= "Dizel",
    ELEKTRIK= "Elektrik",
    HIBRIT ="Hibrit",
    BILINMIYOR="Bilinmiyor ..."

# ARABA
class Araba:

    # CONSTRUCTOR
    def __init__(self, marka: str = "Bilinmiyor", model: str = "Bilinmiyor", yil: str = "1970-01-01", renk: str = "Bilinmiyor", fiyat: float = 0.0, motor_gucu: float = 0.0, yakit_turu: YakitTuru = YakitTuru.BILINMIYOR) -> None:
        self.__marka: str = marka  # private
        self._model: str = model  # protected
        self.yil: datetime = datetime.strptime(yil, '%Y-%m-%d')  # public
        self.renk: str = renk  # public
        self.fiyat: float = fiyat  # public
        self.motor_gucu: float = motor_gucu  # public
        self.yakit_turu: YakitTuru = yakit_turu  # public
        logging.info(f"Yeni araba oluşturuldu: Marka={marka}, Model={model}, Yıl={yil}, Renk={renk}, Fiyat={fiyat}, Motor Gücü={motor_gucu}, Yakıt Türü={yakit_turu.value}")
        print(f"Araba sınıfına {Renk.YESIL.value}  yeni bir araba oluşturuldu.")

    # Destructor
    def __del__(self):
        logging.info(f"Araba silindi: Marka={self.__marka}, Model={self._model}")
        print(f"{Renk.KIRMIZI.value} Araba sınıfından Marka={self.__marka}, {Renk.KIRMIZI.value} Model={self._model} silindi.")


    # METHOD
    def goster_bilgileri(self) -> None:
        logging.info(f"Araba bilgileri gösteriliyor: Marka={self.__marka}, Model={self._model}")
        print(f"Marka: {self.__marka}, Model: {self._model}, Yıl: {self.yil.strftime('%Y-%m-%d')}, Renk: {self.renk}, Fiyat: {self.fiyat:.2f} TL, Motor Gücü: {self.motor_gucu} HP, Yakıt Türü: {self.yakit_turu.value}")
    # Marka SET (private: Çift çizgi)
    # modeling SET (protected: Tek çizgi)
    # yil SET (public: 0 çizgi)

    # SETTER AND GETTER (VALIDATION)
    # METHOD
    def goster_bilgileri(self) -> None:
        logging.info(f"Araba bilgileri gösteriliyor: Marka={self.__marka}, Model={self._model}")
        print(f" {Renk.MAVI.value} Marka: {self.__marka}, Model: {self._model}, Yıl: {self.yil.strftime('%Y-%m-%d')}, Renk: {self.renk}, Fiyat: {self.fiyat:.2f} TL, Motor Gücü: {self.motor_gucu} HP, Yakıt Türü: {self.yakit_turu.value}")

    # SETTER AND GETTER
    # Marka SET
    def set_marka(self, marka: str) -> None:
        if not isinstance(marka, str):
            raise TypeError("Marka bir string olmalıdır.")
        self.__marka = marka
        logging.info(f"Marka güncellendi: {marka}")
        print(f"{Renk.YESIL.value} Marka güncellendi: {marka}")

    def get_marka(self) -> str:
        return self.__marka

    # Model SET
    def set_model(self, model: str) -> None:
        if not isinstance(model, str):
            raise TypeError("Model bir string olmalıdır.")
        self._model = model
        logging.info(f"Model güncellendi: {model}")
        print(f"{Renk.YESIL.value} Model güncellendi: {model}")

    def get_model(self) -> str:
        return self._model

    # Yıl SET
    def set_yil(self, yil: str) -> None:
        if not isinstance(yil, str):
            raise TypeError("Yıl bir string olmalıdır ve 'YYYY-MM-DD' formatında olmalıdır.")
        try:
            self.yil = datetime.strptime(yil, '%Y-%m-%d')
            logging.info(f"Yıl güncellendi: {yil}")
            print(f"{Renk.YESIL.value} Yıl güncellendi: {yil}")
        except ValueError as ve:
            logging.error(f"ValueError: Geçersiz tarih formatı girildi. {ve}")
            print(f"{Renk.KIRMIZI.value}Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında giriniz.{Renk.SIFIRLA.value}")
        finally:
            print(f"{Renk.SARI.value} Tarih işlemi bitti {Renk.SIFIRLA.value}")

    def get_yil(self) -> str:
        return self.yil.strftime('%Y-%m-%d')

    # Renk SET
    def set_renk(self, renk: str) -> None:
        if not isinstance(renk, str):
            raise TypeError("Renk bir string olmalıdır.")
        self.renk = renk
        logging.info(f"Renk güncellendi: {renk}")
        print(f"{Renk.YESIL.value} Renk güncellendi: {renk}")

    def get_renk(self) -> str:
        return self.renk

    # Fiyat SET
    def set_fiyat(self, fiyat: float) -> None:
        if not isinstance(fiyat, (float, int)) or fiyat < 0:
            raise ValueError("Fiyat sıfırdan küçük olamaz ve sayısal bir değer olmalıdır.")
        self.fiyat = float(fiyat)
        logging.info(f"Fiyat güncellendi: {fiyat}")
        print(f"{Renk.YESIL.value} Fiyat güncellendi: {fiyat}")

    def get_fiyat(self) -> float:
        return self.fiyat

    # Motor Gücü SET
    def set_motor_gucu(self, motor_gucu: float) -> None:
        if not isinstance(motor_gucu, (float, int)) or motor_gucu < 0:
            raise ValueError("Motor gücü sıfırdan küçük olamaz ve sayısal bir değer olmalıdır.")
        self.motor_gucu = float(motor_gucu)
        logging.info(f"Motor gücü güncellendi: {motor_gucu}")
        print(f"{Renk.YESIL.value} Motor gücü güncellendi: {motor_gucu}")

    def get_motor_gucu(self) -> float:
        return self.motor_gucu

    # Yakıt Türü SET
    def set_yakit_turu(self, yakit_turu: YakitTuru) -> None:
        if not isinstance(yakit_turu, YakitTuru):
            raise TypeError("Yakıt türü bir YakitTuru enum değeri olmalıdır.")
        self.yakit_turu = yakit_turu
        logging.info(f"Yakıt türü güncellendi: {yakit_turu.value}")
        print(f"{Renk.YESIL.value} Yakıt türü güncellendi: {yakit_turu.value}")

    def get_yakit_turu(self) -> YakitTuru:
        return self.yakit_turu


################################################################################
araba1= Araba()
araba1.goster_bilgileri()

################################################################################
print("#######################################################################")
araba2= Araba()
araba2.set_marka("Audi")
araba2.set_model("A3")
araba2.set_yil("2020-01-01")
araba2.set_renk("Beyaz")
araba2.set_fiyat(25000.0)
araba2.set_motor_gucu(150)
araba2.set_yakit_turu(YakitTuru.DIZEL)
araba2.goster_bilgileri()

################################################################################
print("#######################################################################")
# araba3= Araba()
# araba3.set_marka(1234)     # Error: Marka, string olmalıdır.
# araba3.set_model(1234)  # Error: Model, string olmalıdır.
# araba3.set_yil("2020-13")  # Error: Geçersiz Tarih Formatında yazdınız. Lütfen YYYY-MM-DD şeklinde yazınız

################################################################################
print(f"{Renk.SIFIRLA.value}####################################################")
print("Araba-1 Silindi")
del araba1

print("Araba-2 Silindi")
del araba2
