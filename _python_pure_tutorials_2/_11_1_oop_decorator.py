# Decorator Design Pattern
# Decorator Tasarım Deseni, nesnelerin işlevselliğini dinamik olarak değiştirmek veya genişletmek için kullanılır.
# Nesnelerin temel işlevlerini bozmadan yeni özellikler eklemenizi sağlar.
# Bu desen, Python'da fonksiyon dekoratörleri kullanılarak kolayca uygulanabilir.
# Ancak, nesnelerin işlevselliğini genişletmek için sınıf tabanlı bir yaklaşım da mümkündür.
# Gerçek Hayat Senaryosu
# Bir kafede farklı içeceklerin fiyatlarını hesapladığınızı düşünün.
# İçeceklere dinamik olarak özellikler eklemek istiyorsunuz (örneğin, süt, şeker, çikolata eklemek).
# Temel içeceği değiştirmeden, dekoratörler ile ekstra özellikler ekleyebilirsiniz.

from abc import ABC, abstractmethod

# Temel Bileşen (Base Component)
class Beverage(ABC):
    @abstractmethod
    def cost(self):
        """
        İçeceğin maliyetini döndürür.
        """
        pass

    @abstractmethod
    def description(self):
        """
        İçeceğin açıklamasını döndürür.
        """
        pass

# Concrete Component (Temel İçecek)
class Coffee(Beverage):
    def cost(self):
        return 10

    def description(self):
        return "Kahve"

# Decorator (Süsleyici)
class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete Decorators (Ekstralar)
class MilkDecorator(BeverageDecorator):
    def cost(self):
        return self.beverage.cost() + 2

    def description(self):
        return self.beverage.description() + ", Süt"

class SugarDecorator(BeverageDecorator):
    def cost(self):
        return self.beverage.cost() + 1

    def description(self):
        return self.beverage.description() + ", Şeker"

class ChocolateDecorator(BeverageDecorator):
    def cost(self):
        return self.beverage.cost() + 3

    def description(self):
        return self.beverage.description() + ", Çikolata"

# Örnek Kullanım
# Temel içecek
basic_coffee = Coffee()
print(f"İçecek: {basic_coffee.description()}, Fiyat: {basic_coffee.cost()} TL")

# Süt eklenmiş kahve
milk_coffee = MilkDecorator(basic_coffee)
print(f"İçecek: {milk_coffee.description()}, Fiyat: {milk_coffee.cost()} TL")

# Şeker ve süt eklenmiş kahve
sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"İçecek: {sugar_milk_coffee.description()}, Fiyat: {sugar_milk_coffee.cost()} TL")

# Çikolata, şeker ve süt eklenmiş kahve
chocolate_sugar_milk_coffee = ChocolateDecorator(sugar_milk_coffee)
print(f"İçecek: {chocolate_sugar_milk_coffee.description()}, Fiyat: {chocolate_sugar_milk_coffee.cost()} TL")


# Açıklamalar

# Temel Bileşen:
# Beverage soyut sınıfı, tüm içeceklerin sahip olması gereken cost ve description metodlarını tanımlar.
# Coffee, bu bileşenin somut bir uygulamasıdır.

# Decorator Sınıfı:
# BeverageDecorator, diğer içecekleri sarmalamak için kullanılan bir soyut sınıftır.
# Bu sınıf, içeceklerin işlevselliğini genişletmek için temel alınır.

# Somut Decorator Sınıfları:
# MilkDecorator, SugarDecorator ve ChocolateDecorator gibi sınıflar, içeceklerin fiyatını ve açıklamasını genişletir.
# Her biri cost ve description metodlarını genişleterek işlevsellik ekler.

# Dinamik Genişleme:
# ChocolateDecorator gibi dekoratörler, diğer içecek nesnelerini sarmalar ve işlevselliği genişletir.
# Bu, içeceklerin temel özelliklerini değiştirmeden yeni işlevler eklemenizi sağlar.