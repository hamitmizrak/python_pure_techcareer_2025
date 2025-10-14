################################################################
# GC (Garbarage Collector)
"""Python'da değişkenler bellek yönetimi açısında otomatik olarak işlenir """
# GC: Gereksiz hale gelmiş ve kullanılmayan çöp olan nesleri otomatik olarak siler
data1=44 # Buradaki number1=44 olan ver artık bir çöptür
data1=23


#####################################################################################
#### Type Convesition ###############################################################
number1= input("Lütfen 1.sayıyı giriniz: ")
# number1= input("Lütfen 1.sayıyı giriniz:\n")
number2= input("Lütfen 2.sayıyı giriniz: ")
number3 = int(number1)+int(number2)
print(f"1.sayı:{number1}, 2.sayı:{number2} toplam={number3}")