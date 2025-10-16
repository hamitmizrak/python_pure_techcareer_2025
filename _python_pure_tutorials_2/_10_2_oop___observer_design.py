# Olay tabanlı sistemlerde birden fazla gözlemciyi tek bir olay ile tetiklemek için Observer Pattern örneği yapabiliriz.


# Karmaşık Bir Örnek: Çoklu Yayıncı ve Çoklu Abone
# Aynı sistemde birden fazla yayıncı ve her yayıncıya farklı aboneler tanımlayabilirsiniz.
# Bu durumda, her yayıncı kendi abonelerini yönetir.
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


# İki farklı yayıncı: Spor Haberleri ve Ekonomi Haberleri
sports_publisher = NewsPublisher()
economy_publisher = NewsPublisher()

# Aboneler
email_subscriber1 = EmailSubscriber("sports_fan@example.com")
email_subscriber2 = EmailSubscriber("economy_analyst@example.com")
sms_subscriber1 = SMSSubscriber("555-999-8888")

# Abonelikler
sports_publisher.subscribe(email_subscriber1)
economy_publisher.subscribe(email_subscriber2)
economy_publisher.subscribe(sms_subscriber1)

# Haber Yayını
print("\nSpor Haberleri:")
sports_publisher.notify_subscribers("Spor haberi: Takım kazandı!")

print("\nEkonomi Haberleri:")
economy_publisher.notify_subscribers("Ekonomi haberi: Borsa yükseldi!")

# Kullanım Alanları
# Haber ve Bildirim Sistemleri: Kullanıcıya bilgi göndermek için.
# GUI Uygulamaları: Buton tıklamaları gibi olaylar için.
# Oyun Geliştirme: Oyun olaylarını (ör. skorlama) yönetmek için.
# Observer Design Pattern, olay yönetimini modüler ve yeniden kullanılabilir bir şekilde uygulamanızı sağlar.
# Projelerinizde kullanıcı bildirimleri, mesajlaşma sistemleri veya olay tabanlı mekanizmalar için bu deseni kullanabilirsiniz.
