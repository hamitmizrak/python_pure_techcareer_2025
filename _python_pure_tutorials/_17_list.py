##########################################################################################
#### Data Type List      #################################################################
from itertools import count

# Homojen Yapı
list_data=[1,2,4,3,5,6,7,0]

# Heterojen Yapı
# list_data=[1,2,3,4,5,6,7,8,"Malatya",True,44.23]

# İlk Data (Pozitif indeksleme: Sıfırdan başlar)
print(f"ilk veri ==> {list_data[0]}")

# Sayma
print(f"count ==>  {list_data.count(0)}")

# Son Data
print(f"{list_data[len(list_data)-1]}")
# Negatif indeksleme: -1'den başlar ve tersten gider.
print(f"{list_data[-1]}")

# Dilimleme (Slicing)
print(list_data[1:4])   # [2, 3, 4]     1<=X<=4-1
print(list_data[:4])    # [1, 2, 3, 4]  0<=X<=4-1
print(list_data[::3])   # Her 3 göster  0  3  6 9

# Yeni bir öğe ekleme
list_data.append(44)
print(f"append ==> {list_data}")

# Öğeyi kaldırma Not: 1 başla
list_data.remove(1)
print(f"remove ==> {list_data}")

# Sıralama
list_data.sort()
print(f"sorted ==> {list_data}")

# Ters çevirme
list_data.reverse()
print(f"reversed ==> {list_data}")

# İterasyon (Döngü ile Gezinme)
for item in list_data:
    print(item)


# Liste Anlama (List Comprehension):
squares = [x^2 for x in range(10)]
print(print(f"squares ==> {squares}"), end=" ")  # end ile yanyana yazmak
print()

# `in` ve `not in` Operatörleri:
# Bir öğenin listede olup olmadığını kontrol eder.
print(f"in ==> {2 in list_data}")
print(f"not in ==> {23 not in list_data}")
##################
# İç İçe Listeler (Nested Lists):
nested_list = [[1, 2, 3], [4, 5, 6]]
print(f"nested list{ nested_list[0][1]}")
print(f"nested list {nested_list[1][1]}")


