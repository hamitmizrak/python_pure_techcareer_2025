# public access modifier

# public: kullanımı kolay ancak herkese açık bir yapıya sahiptir.
# Class örneği yaparken new keywordunu kullanmadım.
class Araba:
    marka = "marka yazılmadı"
    model = "model yazılmadı"
    yil= 0
    renk="renk yazılmadı"

    # Method
    # Self Parametresi: Python'da bir metot içinde olan o anki nesneye erişmek için kullanılır.
    def calistir(self):
        print(f"Marka: {self.marka} Model: {self.model} Yıl: {self.yil} Renk: {self.renk}")
################################################################

# Python Sınıf Örneği(instance)
araba1 = Araba()
araba1.calistir()

print("################################################################")
# Python Sınıf Örneği(instance)
araba2 = Araba()
# public access modifier
araba2.marka = "Mercedes"
araba2.model = "E-Class"
araba2.yil = 2021
araba2.renk = "Siyah"
araba2.calistir()