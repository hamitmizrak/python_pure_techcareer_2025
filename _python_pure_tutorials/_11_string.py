#####################################################################################
#### string #########################################################################

# Tek tırnak kullanarak string
metinData = 'metin1'
print(metinData)

# Çift tırnak kullanarak string
metinData2 = "metin2"
print(metinData2)

# Üçlü tırnak kullanarak çok satırlı string (docstring)
metinData3 = """Bu,
birden
fazla satırdan oluşan
bir metindir."""
print(metinData3)

print("##########################################")
#################################################################################################

# 1-) İmmutability (Değişmezlik):
# İmmutability (Değişmezlik): Stringler Python'da immutable (değiştirilemez) veri tipleridir.
# Bir string oluşturulduktan sonra, karakterlerini doğrudan değiştiremezsiniz.
metin1 = "metin4"
# metin4[0] = 'J'  # Hata verir
print(metin1)

print("##########################################")
#################################################################################################

# 2-) Karakter Dizisi (Sequence):
# Karakter Dizisi (Sequence): Stringler birer karakter dizisidir.
# Her bir karakterin bir indeksi vardır ve bu indeks sıfırdan başlar.
metin2 = "metin5"
print(metin2[0])  # P

print(metin2[5])   # n (pozitif indeksle düzden erişim)
print(metin2[-1])  # n (negatif indeksle tersten erişim)

print("##########################################")
#################################################################################################

# 3-) type():
metin3 = 'Malatya Elazığ Bingöl Malatya Bitlis '
print(type(metin3))
print(metin3)

print("##########################################")
#################################################################################################

# 4-) Harf Sayısı
metin4 = 'Malatya '
# HATA: print("kelime sayısı: "+len(kelime))
print("kelime sayısı: ", len(metin4))


print("##########################################")
#################################################################################################

# Çoğaltma (Repetition): * operatörü ile bir string belirli sayıda tekrarlanabilir.
metin5 = 'malatya'
# 5-) Dinamik Uzunluk: Python'da stringlerin uzunluğu dinamik olarak hesaplanabilir.
print("kelime adeti: ", metin5 * 3,sep=" - ")
#################################################################################################

print("##########################################")
# 6-) Unicode Desteği: Python'da stringler Unicode karakterleri destekler.
# Bu nedenle uluslararası metinlerle çalışmak kolaydır.
metin6 = "こんにちは"  # Japonca
print(metin6)

print("##########################################")
#################################################################################################

# 7-) Birleştirme (Concatenation): Stringler + operatörü ile birleştirilebilir.
metin71 = "Python"
metin72 = "Dersi"
# sonuc7 = metin71 + " " + metin72
sonuc7 = metin71 +" "+ metin72
print(sonuc7)  # Python Dersi

#################################################################################################

# 8-) join(iterable)
# Iterable (liste, tuple, vb.) içindeki elemanları bir stringle birleştirir.
liste = ["Python", "join"]
print(liste[0] + " "+ liste[1] )
print(" ".join(liste))  # Python Dersi

print("##########################################")
#################################################################################################

# 9-) Parçalama (Slicing): Stringlerin belirli bir kısmını alabilirsiniz.
metin8 = "Python"
print(metin8[1:4])  # yth  1<=X<4

print(metin8[0:3])  # Pyt 0<=X<3
print(metin8[:3])   # Pyt 0<=X<3

print(metin8[3:])     # hon
# print(metin8[3:])   # hon


print("##########################################")
#################################################################################################

# 10-) String Formatlama: Dinamik değerler eklemek için format() veya f-string kullanılır.
name = "Hamit"
surname = "Mızrak"
print(f"Merhaba, benim adım {name} soyadım {surname}")


print("##########################################")
#################################################################################################

# 11-) Arama ve Değiştirme:
# Alt stringin, ana string içinde ilk geçtiği indeksini döner.
# Alt string bulunamazsa -1 döner.
# find(): Alt string arar.

metin10 = "Python programlama dili"
print(metin10.find("programlama"))

print("##########################################")
#################################################################################################


# 12-) replace(): Belirli bir alt stringi başka bir string ile değiştirir.
print(metin10.replace("Python", "Java"))  # Java programlama dili

print("##########################################")
#################################################################################################

# 13-) UPPER
metin11 = "Python programlama dili"
print("Büyük Harf: ", metin11.upper())
print("Hepsi Büyük Harf: ", metin11.isupper())
print("Hepsi Büyük Harf: ", metin11.upper().isupper())

print("##########################################")
#################################################################################################

# 14-) LOWER
metin12 = "Python programlama dili"
print("Küçük Harf: ", metin12.lower())
print("Hepsi Küçük Harf: ", metin12.islower())
print("Hepsi Küçük Harf: ", metin12.lower().islower())


print("##########################################")
#################################################################################################

# 15. casefold()
# Stringin tüm karakterlerini küçük harfe dönüştürür.
# Unicode karakterler için büyük-küçük harf dönüşümlerinde daha güçlüdür.
metin122 = "ß"
print(metin122.casefold())  # ss

print("##########################################")
#################################################################################################

# 16 endswith(suffix, start, end)
# Stringin belirtilen bir alt string ile bitip bitmediğini kontrol eder.
metin122 = "Merhaba Python"
print(metin122.endswith("Python"))  # True

print("##########################################")
#################################################################################################


# 17 startswith(suffix, start, end)
print(metin122.startswith("Python"))  # True

print("##########################################")
#################################################################################################

# 18 index(substring, start, end)
# Alt stringin, ana string içinde ilk geçtiği indeksini döner.
# Alt string bulunamazsa hata verir (ValueError).
metin125 = "Python öğren, Python uygula"
print(metin125.index("öğren"))  # 7

print("##########################################")
#################################################################################################

# 19-) CAPITALIZE
# Stringin sadece ilk karakterini BÜYÜK, diğerlerini küçük yapar.
# Çoğunlukla cümle başlıkları oluşturmak için kullanılır.
metin13 = "programlama datası"
print("capitalize:", metin13.capitalize())  # Programlama

print("##########################################")
#################################################################################################

# 20-) TITLE
# Her kelimenin ilk harfini büyük yapar.
metin14 = "ilk karakter büyük olsun."
print("title:", metin14.title())

print("##########################################")
#################################################################################################

# 22-) strip:
# Başındaki ve sonundaki boşlukları kaldırır.
metin15 = "Python programlama dili"
print("trimsiz: ", metin15)
print("trimsiz len: ", len(metin15))
print("trimli: ", metin15.strip())
print("trimli len: ", len(metin15.strip()))

print("##########################################")
#################################################################################################

# 23-) split()	Stringi belirli bir ayırıcıya göre böler.
metin16 = "Python programlama dili"
metin162 = []
metin162 = metin16.split()
print(metin162)
print(metin162[0])
print(metin162[1])
print(metin162[2])

print("##########################################")
#################################################################################################

# 24-) String ve Döngüler:
# Stringler üzerinde döngü kullanarak her bir karaktere erişebilirsiniz:
metin17 = "String Döngüsü Python"
for temp in metin17:
    print(temp)

print("##########################################")
#################################################################################################

# 25-) Stringlerin Unicode kod noktalarına erişmek için ord()
#  ve karakterlerden string oluşturmak için chr() kullanılabilir.
print(ord('A'))  # 65
print(chr(65))   # A

print("##########################################")
#################################################################################################

# 26-) Stringlerin Bellekte Temsili
# Python'da stringler bellekte immutable olduğu için her değişiklik yeni bir string oluşturur.
metin19 = "Merhaba"
yeni_metin20 = metin19 + " Dünya"
print(f"Orijinal stringin id {id(metin19)}")  # Orijinal stringin id'si
print(f"Yeni stringin id'si  {id(yeni_metin20)}")

print("##########################################")
#################################################################################################

# 27-) Stringler üzerinde düzenli ifadelerle güçlü arama ve değiştirme işlemleri yapabilirsiniz:
import re

metin = "Python 101 dersi"
pattern = r"\d+"
sonuc = re.findall(pattern, metin)
print(sonuc)  # ['101']

# import re: Python'un düzenli ifadeler (regex) ile çalışmasını sağlayan re modülünü içe aktarır.
# metin = "Python 101 dersi": metin adında bir string değişken tanımlar.
# pattern = r"\d+":
# \d : Bir rakamı ifade eder (0-9).
# + : Bir veya daha fazla rakamın eşleşmesini sağlar.
# r : Raw string literal (ham string) tanımıdır, ters eğik çizgiyi (\) özel bir karakter olarak değil, doğrudan regex deseni olarak işler.
# re.findall(pattern, metin):
# findall fonksiyonu, verilen metin içinde regex desenine uyan tüm eşleşmeleri bulur ve bir liste olarak döner.


print("##########################################")
#################################################################################################

# 28-) İleri Düzey Formatlama:
# Raw String: r"metin" şeklinde tanımlanır, kaçış karakterlerini yok sayar.
print(r"C:\kullanıcı\dosya")  # Kaçış karakteri işlenmez
print(r"C:\kullanıcı\dosya\naltsatır")   # Kaçış karakteri işlenmez
# print("C:\kullanıcı\dosya\naltsatır")  # Kaçış karakteri işlenmez


print("##########################################")
#################################################################################################

# 29-) center(width, char)
# Stringi belirli bir genişliğe göre ortalar ve etrafını belirtilen karakterle doldurur.
metin22 = "Python"
print(metin22.center(20, '*'))  # *******Python*******

print("##########################################")
#################################################################################################

# 30-) count(substring, start, end)
# String içinde bir alt stringin kaç kez geçtiğini döner.
# Alt stringin, ana string içinde kaç kez geçtiğini döner.
# İsteğe bağlı olarak başlangıç ve bitiş indeksleri belirtilebilir.
metin23 = "Python öğren, Python uygula"
search23 = "Python"
print(search23 + " kelimesi: ", metin23.count(search23))  # 2

print("##########################################")
#################################################################################################

# 31-) encode(encoding, errors)
# Stringi belirtilen bir kodlamaya göre (örneğin, UTF-8) kodlar.
# encode(encoding="utf-8", errors="strict")
# Stringi belirtilen kodlamaya dönüştürür.
# errors parametresi ile hata işleme yöntemi belirlenir.
metin24 = "Python"
print(metin24.encode("utf-8"))  # b'Python'

print("##########################################")
#################################################################################################

# 32-) expandtabs(tabsize)
# Stringdeki tab karakterlerini (\t) belirtilen sayıda boşlukla değiştirir.
metin25 = "Python\tProgramlama"
print(metin25.expandtabs(50))  # Python    Programlama

print("##########################################")
#################################################################################################

# 33-) isalnum()
# Stringin sadece harf ve rakam içerip içermediğini kontrol eder.
# metin26 = "Python"
metin26 = "Python44"
print(metin26.isalnum())  # True

print("##########################################")
#################################################################################################

# 34-) isalpha()
# Stringin sadece harf içerip içermediğini kontrol eder.
metin27 = "Python"
print("Sadece harf mi ?", metin27.isalpha())  # True

print("##########################################")
#################################################################################################

# 35-)  isdigit()
# Stringin sadece rakam içerip içermediğini kontrol eder.
metin28 = "12345"
print("Sadece sayı mi ?", metin28.isdigit())  # True

# # Metot () dir: Fonksiyon okur yazarlığı için
# # print(dir("java"));
#
# #  Üyelik Operatörleri ==> in, not in
# #  Kimlik Operatörleri ==> is, is not
