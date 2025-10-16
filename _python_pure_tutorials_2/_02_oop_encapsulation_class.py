
# Encapsulation GET,SET

# Python'da yapıcı metot: __init__ bu metot
# __init__: Bir sınıf örneğimizi oluşturduğumuzda __init__ olan metot otomatik çağrılır.
# Self Parametresi: Python'da bir metot içinde olan o anki nesneye erişmek için kullanılır.

class Araba:

    # Constructor
    def __init__(self, marka="Bilinmiyor", model="Bilinmiyor",yil=0, renk="Bilinmiyor"):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.renk=renk
        print("Araba sınıfına yeni bir araba oluşturuldu.")

    # METHOD
    def goster_bilgileri(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}, Renk: {self.renk}")

    # SETTER AND GETTER
    # Marka SET
    def set_marka(self,marka):
        self.marka=marka

    def get_marka(self):
        return self.marka

    # Model SET
    def set_model(self,model):
        self.model=model

    def get_model(self):
        return self.model

    # Yıl SET
    def set_yil(self,yil):
        if yil >=2015:
            self.yil=yil
        else:
            print("2015 altındaki arabaları almıyoruz.")

    def get_yil(self):
        return self.yil

    # Renk SET
    def set_renk(self,renk):
        self.renk=renk

    def get_renk(self):
        return self.renk

#########################################################################
print("################################################################")
araba1= Araba()
araba1.goster_bilgileri()
print("################################################################")

#########################################################################
# Araba nesnesi için set/get ile yönetmek
araba2= Araba()
# private access modifier
araba2.set_marka("Toyota")
araba2.set_model("Corolla")
araba2.set_yil(2020)
araba2.set_renk("Siyah")
araba2.goster_bilgileri()
print("################################################################")

araba3= Araba()
araba3.set_yil(2000)
araba3.goster_bilgileri()






