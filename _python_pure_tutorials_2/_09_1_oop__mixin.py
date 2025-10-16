# Birden fazla sınıfın ortak fonksiyonelliğini paylaşmak için Mixin sınıfları oluşturabiliriz.

# Mixin sınıfları, çoklu kalıtım kullanarak bir sınıfa yeni işlevsellik eklemek için kullanılır.
# Mixin'ler genellikle küçük, yeniden kullanılabilir işlevsellik bloklarıdır ve bir sınıfın ana işlevini değiştirmeden ek özellikler sağlar.
# Mixin'ler bağımsızdır ve tek başına kullanılmazlar. Diğer sınıflarla birleştirilerek işlevsellik eklerler.

# Örnek: LoggerMixin ile Loglama Eklemek
# Bir uygulamada farklı sınıflara loglama özelliği eklemek istediğimizi düşünelim.
# Bunun için bir LoggerMixin oluşturabiliriz.

import datetime

# Mixin Sınıfı
class LoggerMixin:
    def log(self, message):
        """
        Loglama işlemini gerçekleştirir.
        """
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] {message}")


# Temel Bir Sınıf
class User:
    def __init__(self, username):
        self.username = username

    def get_user_info(self):
        return f"Kullanıcı: {self.username}"


# LoggerMixin ile Birleştirilmiş Sınıf
class LoggedUser(User, LoggerMixin):
    def login(self):
        self.log(f"{self.username} giriş yaptı.")

    def logout(self):
        self.log(f"{self.username} çıkış yaptı.")


# Örnek Kullanım
user = LoggedUser("example_user")
print(user.get_user_info())
user.login()
user.logout()


# Açıklamalar
# Mixin Tanımı:
#
# LoggerMixin sınıfı, loglama özelliğini sağlıyor.
# Başka sınıflarla birleştirildiğinde, bu sınıflara loglama yeteneği ekliyor.
# Temel Sınıf:
#
# User sınıfı, kullanıcı bilgilerini tutuyor.
# Sadece kendi işlevine odaklanıyor.
# Mixin Kullanımı:
#
# LoggedUser sınıfı, hem User hem de LoggerMixin sınıfından kalıtım alıyor.
# Böylece LoggerMixin'in loglama özelliğini kazanıyor.
# Çoklu Kalıtım:
#
# Mixin'ler genellikle başka bir sınıfla birlikte kullanılır.
# Temel işlevselliği değiştirmeden ek özellik sağlar.
# Daha Karmaşık Bir Örnek: JSON ve CSV Desteği Ekleyen Mixin
# Bir veri sınıfına hem JSON hem de CSV formatında çıktı verme özelliği eklemek için iki ayrı Mixin kullanılabilir.


# Bu Örneklerin Avantajları
# Yeniden Kullanılabilirlik: Loglama, JSON ve CSV çıktısı gibi özellikler farklı sınıflar için kolayca eklenebilir.
# Modülerlik: Her Mixin sınıfı tek bir işlevselliğe odaklanır.
# Çoklu Kalıtım ile Birleşim: Ana sınıfın temel işlevine odaklanmasını sağlar ve gereksiz karmaşıklıktan kaçınılır.
# Mixin'ler, projelerde kodun daha düzenli ve modüler olmasını sağlayarak, DRY (Don't Repeat Yourself) prensibini uygular.
