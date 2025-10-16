##########################################################################################
#### Data Type : Tuple      ##############################################################
# Python'da tuple (demet), birden fazla öğeyi sıralı bir şekilde saklayabilen, ancak immutable (değiştirilemez) bir veri türüdür.
# Listelere benzer şekilde, tuple da öğeleri sıralı bir şekilde saklar ve indekslenebilir.
# Ancak list ile  tuple'ın en büyük farkı, oluşturulduktan sonra içeriğinin değiştirilemez olmasıdır.

# Boş bir tuple
empty_tuple = ()

#  Tek öğeli tuple
# DİKKAT: Tek öğeli bir tuple oluştururken, parantez içindeki öğeden sonra virgül koyulmazsa,
# Python bunu tuple olarak algılamaz.
single_element_tuple = (5,)
# not_a_tuple = (1)   # Bu bir tamsayıdır.
a_tuple = (1,)      # Bu bir tuple'dır.

# Birden fazla öğe içeren tuple
multi_tuple = (1, 2, 3, 4)


################################################################
# Tuple ile İndeksleme ve Dilimleme
# 1. İndeksleme:
#    - Pozitif indeksleme: Sıfırdan başlar.
#    - Negatif indeksleme: -1'den başlar.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # Çıktı: 10
print(my_tuple[-1]) # Çıktı: 50

# 2.Dilimleme(Slicing):
# - Tuple
# 'ın belli bir kısmını almak için `başlangıç:bitis:adım` kullanılır.
# - Örnek:
print(my_tuple[1:4])    # Çıktı: (20, 30, 40)
print(my_tuple[:3])     # Çıktı: (10, 20, 30)
print(my_tuple[::2])    # Çıktı: (10, 30, 50)


# Sayma
print(my_tuple.count(2))   # Çıktı: 2

# İndeks bulma
# print(my_tuple.index(1))   # Çıktı: 2

################################################################
# 1- Koordinatlar veya Sabit Değerler Saklama:
coordinates = (10.0, 20.0)
print(f"Koordinatlar: {coordinates}")

# 2. Birden Fazla Değeri Fonksiyon ile Döndürme:
def person_info():
    return "Ali", 30, "Mühendis"

name, age, job = person_info()
print(name,age,job)
# Çıktı: Ali

# 3. Tuple ile Döngü:
my_tuple = ("Python", "Java", "C++")
for lang in my_tuple:
   print(lang)

# 4. Liste ve Tuple Dönüşümleri:
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)
# Çıktı: (1, 2, 3)

my_new_list = list(my_tuple)
print(my_new_list)
# Çıktı: [1, 2, 3]

# `in` ve `not in` Operatörleri:
# - Bir öğenin tuple içinde olup olmadığını kontrol eder.

my_tuple = (1, 2, 3)
print(2 in my_tuple)      # Çıktı: True
print(4 not in my_tuple)  # Çıktı: True
