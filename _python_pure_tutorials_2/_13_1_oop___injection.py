# Dependency Injection (Bağımlılık Enjeksiyonu)
# Dependency Injection (DI), nesneler arası bağımlılıkların başka bir sınıf tarafından sağlandığı bir tasarım desenidir.
# Bu yöntem, bağımlılıkların sınıf içinde değil, dışarıdan geçirilmesiyle uygulanır.
# DI, kodun test edilebilirliğini artırır, modülerliği geliştirir ve sıkı bağımlılıkları gevşetir.

# Temel Yapı
# DI, üç farklı yöntemle uygulanabilir:

# Constructor Injection: Bağımlılıklar, nesne oluşturulurken yapıcı (constructor) aracılığıyla sağlanır.
# Setter Injection: Bağımlılıklar, setter metotları aracılığıyla sağlanır.
# Interface Injection: Bağımlılıklar, bir arayüz aracılığıyla sağlanır.

# Python'da Dependency Injection Örneği
# Senaryo
# Bir uygulama, veri kaydetmek için farklı türde veri depolama yöntemlerini (örneğin, dosya veya veritabanı) destekliyor.
# Dependency Injection, veri depolama yöntemini dışarıdan sağlayarak modüler bir yapı sağlar.

from abc import ABC, abstractmethod

# Veri Kaydetme Arayüzü
class DataStorage(ABC):
    @abstractmethod
    def save(self, data):
        """
        Veriyi kaydetmek için soyut metot.
        """
        pass

# Dosyaya Veri Kaydetme (Concrete Implementation)
class FileStorage(DataStorage):
    def save(self, data):
        print(f"Dosyaya kaydedildi: {data}")

# Veritabanına Veri Kaydetme (Concrete Implementation)
class DatabaseStorage(DataStorage):
    def save(self, data):
        print(f"Veritabanına kaydedildi: {data}")

# İşlem Yapan Sınıf
class DataProcessor:
    def __init__(self, storage: DataStorage):
        """
        Constructor Injection ile bağımlılığı sağlıyoruz.
        """
        self.storage = storage

    def process_and_save(self, data):
        # Veriyi işleyip kaydediyoruz
        processed_data = f"İşlenmiş: {data}"
        self.storage.save(processed_data)
# Kullanım
# Dosya depolama kullanarak işlem
file_storage = FileStorage()
processor_with_file = DataProcessor(file_storage)
processor_with_file.process_and_save("Python Dependency Injection")
# Çıktı: Dosyaya kaydedildi: İşlenmiş: Python Dependency Injection

# Veritabanı depolama kullanarak işlem
db_storage = DatabaseStorage()
processor_with_db = DataProcessor(db_storage)
processor_with_db.process_and_save("Python Dependency Injection")
# Çıktı: Veritabanına kaydedildi: İşlenmiş: Python Dependency Injection




# Açıklamalar

# Soyutlama (Abstraction):
# DataStorage, tüm veri depolama yöntemlerinin sahip olması gereken save metodunu tanımlar.
# Bu, uygulamanın farklı veri depolama yöntemlerine karşı bağımsız olmasını sağlar.

# Concrete Implementation:
# FileStorage ve DatabaseStorage sınıfları, DataStorage arayüzünü genişleterek somut davranışları tanımlar.

# Constructor Injection:
# DataProcessor sınıfı, bağımlılıklarını yapıcı (__init__) metodu aracılığıyla alır.
# Bu, bağımlılıkların test sırasında veya gerçek uygulama sırasında kolayca değiştirilmesine olanak tanır.

# Esneklik:
# DataProcessor sınıfı, veri depolama yöntemine dair hiçbir bilgi içermez. Hangi depolama yöntemi kullanılıyorsa,
# o sınıfın bir örneği dışarıdan sağlanır.
# Gelişmiş Kullanım: DI Framework
# Daha karmaşık projelerde manuel bağımlılık yönetimi zor olabilir.
# Bu nedenle, bir Dependency Injection Framework kullanmak işleri kolaylaştırabilir.
# Python'da inject veya dependency-injector gibi kütüphaneler bu işi kolaylaştırır.