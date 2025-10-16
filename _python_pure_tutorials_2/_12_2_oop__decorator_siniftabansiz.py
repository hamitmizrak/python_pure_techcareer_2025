# Decorator fonksiyonunu, sınıf tabanlı bir tasarımla birleştirebilirsiniz.
# Ancak bu iki yapının bir araya getirilmesi, kullanım amacına ve bağlama bağlıdır.
# Sınıf tabanlı bir sistemde,
# yetki kontrolü işlevini bir sınıfın veya metodun davranışına entegre etmek için decorator’ü sınıf tabanlı yapıya dönüştürebiliriz.
#
# Sınıf ve Fonksiyon Dekoratörlerini Birleştirme
# Aşağıda, authorize fonksiyonunu sınıf tabanlı yapıya dahil ederek birleştirilmiş bir çözüm yer almaktadır:


from abc import ABC, abstractmethod

# Yetki Kontrol Dekoratörü
def authorize(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") == role:
                return func(user, *args, **kwargs)
            else:
                return f"Erişim reddedildi! {role} yetkisi gerekiyor."
        return wrapper
    return decorator

# Kullanıcı Arayüzü (Abstract Class)
class UserInterface(ABC):
    @abstractmethod
    def get_role(self):
        """
        Kullanıcının rolünü döndürür.
        """
        pass

# Kullanıcı Sınıfı
class User(UserInterface):
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def get_role(self):
        return self.role

# Panel Görüntüleme Sınıfı
class AdminPanel:
    @authorize("admin")
    def view(self, user: User):
        """
        Admin paneline giriş işlemi.
        """
        return f"Hoş geldiniz, {user.username}! Admin panelindesiniz."

# Örnek Kullanım
# Kullanıcılar
admin_user = User("admin_user", "admin")
regular_user = User("regular_user", "user")

# Admin Paneli
panel = AdminPanel()

# Admin yetkisi olan kullanıcı
print(panel.view(admin_user))  # Çıktı: Hoş geldiniz, admin_user! Admin panelindesiniz.

# Admin yetkisi olmayan kullanıcı
print(panel.view(regular_user))  # Çıktı: Erişim reddedildi! admin yetkisi gerekiyor.


# Açıklamalar

# Fonksiyon Dekoratörü:
# authorize fonksiyonu, belirli bir rol kontrolü sağlar.
# Metotlar üzerinde doğrudan kullanılabilir.

# Abstract Base Class (UserInterface):
# UserInterface, tüm kullanıcı sınıflarının bir get_role metodu sağlamasını zorunlu kılar.


# Kullanıcı Sınıfı:
# User, UserInterface'den türetilmiştir ve get_role metodu üzerinden rol bilgisini sağlar.


# Panel Görüntüleme:
# AdminPanel sınıfındaki view metodu, authorize dekoratörü ile süslenmiştir.
# Yalnızca admin rolüne sahip kullanıcılar bu metodu başarıyla çalıştırabilir.

# Avantajlar
# Esneklik: Hem fonksiyon hem de sınıf tabanlı bir sistemde birlikte çalışır.
# Yeniden Kullanılabilirlik: authorize dekoratörü, sınıf metodlarında ve fonksiyonlarda tekrar tekrar kullanılabilir.
# Modülerlik: Kullanıcı rolleri ve yetkilendirme işlevleri ayrı bir sistemde düzenlenir.
# Genişletilebilirlik: Yeni roller veya işlevler kolayca eklenebilir.
# Eğer aynı yetkilendirme mantığını birden fazla sınıfta/metotta kullanmak istiyorsanız, bu yaklaşım uygundur.
# Ancak daha karmaşık senaryolar için yetkilendirme mantığını tamamen bir middleware veya
# servis tabanlı bir yapıya taşımayı düşünebilirsiniz.