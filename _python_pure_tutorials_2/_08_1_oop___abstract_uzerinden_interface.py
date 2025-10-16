# Python'da arayüz kavramı, Java gibi dillerdeki kadar doğrudan bir şekilde desteklenmez.
# Ancak, soyut sınıflar (Abstract Base Classes, abc modülü) kullanılarak arayüz benzeri bir yapı oluşturulabilir.
# Arayüz, sınıfların belirli bir davranış kümesini uygulamalarını zorunlu kılmak için kullanılır.

# İşte Python'da arayüz kullanımına dair bir örnek:
# Örnek: Ödeme Sistemlerinde Arayüz Kullanımı
# Bir e-ticaret uygulamasında farklı ödeme yöntemlerini (kredi kartı, PayPal, banka transferi) desteklemek istediğimizi düşünelim.
# Bunun için bir PaymentInterface arayüzü tanımlayabiliriz.

from abc import ABC, abstractmethod

# Arayüz (Interface)
class PaymentInterface(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """
        Ödemenin işlenmesini sağlayan bir metot.
        Her alt sınıf bu metodu uygulamak zorundadır.
        """
        pass

    @abstractmethod
    def validate_payment(self):
        """
        Ödemenin geçerli olup olmadığını kontrol eden metot.
        """
        pass

# Kredi Kartı Ödeme Sınıfı
class CreditCardPayment(PaymentInterface):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Kredi kartı ile {amount} TL ödeme işleniyor. Kart numarası: {self.card_number}.")

    def validate_payment(self):
        print("Kredi kartı bilgileri doğrulandı.")

# PayPal Ödeme Sınıfı
class PayPalPayment(PaymentInterface):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        print(f"PayPal ile {amount} TL ödeme işleniyor. PayPal hesabı: {self.email}.")

    def validate_payment(self):
        print("PayPal hesabı doğrulandı.")

# Banka Transferi Ödeme Sınıfı
class BankTransferPayment(PaymentInterface):
    def __init__(self, iban):
        self.iban = iban

    def process_payment(self, amount):
        print(f"Banka transferi ile {amount} TL ödeme işleniyor. IBAN: {self.iban}.")

    def validate_payment(self):
        print("Banka transfer bilgileri doğrulandı.")

# Arayüzün Kullanımı
def make_payment(payment_method: PaymentInterface, amount: float):
    payment_method.validate_payment()
    payment_method.process_payment(amount)

# Örnek Kullanım
credit_card = CreditCardPayment("1234-5678-9012-3456")
paypal = PayPalPayment("user@example.com")
bank_transfer = BankTransferPayment("TR00 0000 0000 0000 0000 0000 00")

print("Kredi Kartı ile Ödeme:")
make_payment(credit_card, 150.0)

print("\nPayPal ile Ödeme:")
make_payment(paypal, 200.0)

print("\nBanka Transferi ile Ödeme:")
make_payment(bank_transfer, 500.0)

# Açıklamalar
# Arayüz Tanımı: PaymentInterface bir soyut sınıf olarak tanımlandı ve iki metot içeriyor: process_payment ve validate_payment.
# Bu metodlar, alt sınıflar tarafından uygulanmak zorunda.

# Alt Sınıflar: Her ödeme yöntemi için (CreditCardPayment, PayPalPayment, BankTransferPayment) ayrı bir sınıf oluşturuldu
# ve bu sınıflar PaymentInterface'den türetildi.

# Polimorfizm: make_payment fonksiyonu, PaymentInterface tipindeki tüm nesnelerle çalışabilir.
# Hangi sınıfın örneği olduğunu bilmesine gerek yoktur.
# Bu yapı sayesinde yeni bir ödeme yöntemi eklemek istediğimizde, PaymentInterface'i genişleten
# bir sınıf oluşturmamız yeterli olacaktır.
