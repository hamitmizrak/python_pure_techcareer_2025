# Olay tabanlı sistemlerde birden fazla gözlemciyi tek bir olay ile tetiklemek için Observer Pattern örneği yapabiliriz.


# Observer Design Pattern
# Observer Tasarım Deseni, bir nesnedeki değişikliklerin, o nesneye bağlı olan diğer nesnelere otomatik olarak bildirilmesini sağlar.
# Bu, olay tabanlı programlama için yaygın bir desendir. Observer Pattern, yayıncı-abone (publisher-subscriber) modeliyle çalışır.

# Gerçek Hayat Senaryosu
# Bir haber sitesinde yeni bir haber yayınlandığında, abone olan kullanıcılar bu haberi alır.
# Publisher haberleri yayınlayan bir sınıfken, Subscriber ise haberleri alan bir sınıftır.
from abc import ABC, abstractmethod

# Observer (Abone) Arayüzü
class Subscriber(ABC):
    @abstractmethod
    def update(self, message):
        """
        Abonelere gönderilecek mesajı işleyen metot.
        """
        pass

# Concrete Observer (Gerçek Aboneler)
class EmailSubscriber(Subscriber):
    def __init__(self, email):
        self.email = email

    def update(self, message):
        print(f"Email gönderildi: {self.email} - Mesaj: {message}")

class SMSSubscriber(Subscriber):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def update(self, message):
        print(f"SMS gönderildi: {self.phone_number} - Mesaj: {message}")

# Subject (Yayıncı) Sınıfı
class NewsPublisher:
    def __init__(self):
        self.subscribers = []  # Aboneleri saklar

    def subscribe(self, subscriber):
        """
        Yeni bir abone ekler.
        """
        self.subscribers.append(subscriber)
        print(f"Yeni abone eklendi: {subscriber}")

    def unsubscribe(self, subscriber):
        """
        Abonelikten çıkarır.
        """
        self.subscribers.remove(subscriber)
        print(f"Abone çıkarıldı: {subscriber}")

    def notify_subscribers(self, message):
        """
        Tüm abonelere mesaj gönderir.
        """
        for subscriber in self.subscribers:
            subscriber.update(message)

# Örnek Kullanım
# Yayıncı oluştur
publisher = NewsPublisher()

# Aboneler oluştur
email_subscriber = EmailSubscriber("user@example.com")
sms_subscriber = SMSSubscriber("555-123-4567")

# Aboneleri ekle
publisher.subscribe(email_subscriber)
publisher.subscribe(sms_subscriber)

# Haber yayınla
print("\nHaber Yayını:")
publisher.notify_subscribers("Yeni haber: Python Observer Pattern!")

# Abonelikten çıkar
publisher.unsubscribe(email_subscriber)

# Haber yayınla
print("\nHaber Yayını (Sonra):")
publisher.notify_subscribers("Bir başka haber!")

# Publisher (Yayıncı):
#
# NewsPublisher sınıfı, haber yayınlamak ve aboneleri yönetmekten sorumludur.
# Aboneleri bir listede tutar (self.subscribers).
# notify_subscribers metodu, abonelere mesaj gönderir.
# Subscriber (Abone):
#
# Subscriber soyut sınıfı, tüm abonelerin sahip olması gereken update metodunu tanımlar.
# EmailSubscriber ve SMSSubscriber, bu arayüzü genişleterek kendi update davranışlarını uygular.
# Dinamik Abonelik:
#
# subscribe metodu yeni aboneleri listeye ekler.
# unsubscribe metodu aboneleri listeden çıkarır.
# Bildirim Mekanizması:
#
# Yayıncı, notify_subscribers metoduyla tüm abonelere mesaj gönderir.
# Hangi tür aboneler olduğuna bakmaksızın update metodu çağrılır.
