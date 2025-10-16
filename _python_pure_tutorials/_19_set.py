##########################################################################################
#### Data Type : Set      ################################################################

# Python'da set (küme), sıralı olmayan, eşsiz (unique) öğelerden oluşan ve mutable (değiştirilebilir) bir veri yapısıdır.

# Boş bir set (set() kullanılmalı, {} boş dictionary oluşturur)
empty_set = set()


# Set
my_set1 = {1, 2, 2, 3}
print(my_set1)

# Not: Setler sırasızdır(Unordered). Yani öğeler belirli bir sırada saklanmaz ve indeksleme kullanılamaz.
# Liste veya başka bir iterable'dan set oluşturma
list_to_set = set([1, 2, 2, 3])
print(list_to_set)   # Çıktı: {1, 2, 3}

#######################################################################################
# add, removed
my_set = {1, 2, 3}

# add
my_set.add(4)
print(my_set)


# Çıktı: Öğe ve güncellenmiş set
removed = my_set.pop()
print(removed)
print(my_set)
# print(removed, my_set)

#######################################################################################
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union: Birleşim
print(set1.union(set2))   #Çıktı: {1, 2, 3, 4, 5}

# intersection: kesişim
print(set1.intersection(set2))   # Çıktı: {3}

# difference : fark
print(set1.difference(set2)) # Çıktı: {1, 2}

 # Simetrik Fark
print(set1.symmetric_difference(set2))   #Çıktı: {1, 2, 4, 5}

#####################################################################
#  Set ile Döngüler ve İterasyon
for item in my_set:
    print(item)

#####################################################################
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 1. Birleşim (`|`):
# - İki setin birleşimini döner.
print(set1 | set2)   #Çıktı: {1, 2, 3}

# 2. Kesişim (`&`):
# - İki setin kesişimini döner.
print(set1 & set2)   #Çıktı: {2}

# 3. Fark (`-`):
# - Bir setin diğerinden farkını döner.
print(set1 - set2)   #Çıktı: {1}

####################################################################
# Frozen set, set'in immutable (değiştirilemez) bir versiyonudur.
# Normal setlerde olduğu gibi eşsiz öğeler içerir,
# ancak bir kez oluşturulduktan sonra içeriği değiştirilemez.
frozen = frozenset([1, 2, 3])
print(frozen)   #Çıktı: frozenset({1, 2, 3})

# Değiştirmeye çalışırsanız hata alırsınız
# frozen.add(4)   #AttributeError





