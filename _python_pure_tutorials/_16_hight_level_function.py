##########################################################################################
#### Hight Level Function#################################################################
from itertools import zip_longest, chain

sayilar= [9,1,2,3,4,5,6]

# 1- map(function, iterable)
# Bir fonksiyonu bir iterable’ın her öğesine uygular ve sonuçları yeni bir iterable olarak döndürür.
map_result= map(lambda x:x*2, sayilar)
# print(f"{map_result}")
print(list(map_result))

# 2- filter(function, iterable)
# Bir fonksiyonu bir iterable’ın öğelerine uygular ve yalnızca `True` döndürenleri filtreler.
filter_result =filter(lambda x:x%2==0, sayilar)
print(list(filter_result))

# 3- reduce(function, iterable, initializer)
# Bir fonksiyonu bir iterable’ın öğelerine soldan sağa doğru uygular ve tek bir değer döndürür.
from functools import reduce
reduce_result= reduce(lambda x,y:x+y, sayilar)
print(reduce_result)

# 4- sorted(iterable, key=None, reverse=False), reversed(iterable)
# Bir iterable’ı belirli bir kritere göre sıralar ve sıralanmış bir liste döndürür.
# Küçükten Büyüğe
print("Küçükten Büyüğe: ", sorted(sayilar))
# Büyükten Küçüğe
print("Tersten yazdır  : ",list(reversed(sayilar)))
print("Büyükten Küçüğe : ",list(reversed(sorted(sayilar))))

# 5- zip(): İki veya daha fazla iterable’ı birleştirerek bir dizi tuple oluşturur.
# zip_longest(): Birden fazla iterable’ı birleştirir, eksik değerler için bir doldurma değeri kullanır.
# itertools.chain(): Birden fazla iterable’ı ardışık bir iterable haline getirir.
isimler = ["Ali", "Ayşe"]
yaslar = [25, 30,44]
print("zip:",list(zip(isimler, yaslar)))
print("zip_longest:",list(zip_longest(isimler, yaslar,fillvalue='?')))
print(list(chain(isimler, yaslar)))

# 6 -
name=["Ahmet","Nalan"]
city=["Malatya","Elazığ"]
# next() : Bir iterator’un bir sonraki öğesini döndürür.
iterator= iter(city)
print(next(iterator))
# list() :
print(list(range(3)))
# set()  :
print(set(name))
# dict() :
# print(dict(name))

# 6- min(iterable), max(iterable), len(iterable), sum(iterable, start=0)
print(f"min: {min(sayilar)}")
print(f"max: {max(sayilar)}")
print(f"len: {len(sayilar)}")
print(f"sum: {sum(sayilar)}")


# 7- isinstance(): Bir nesnenin belirli bir veri tipine ait olup olmadığını kontrol eder.
# type:
print("5 sayısı türü", type(5))
print("5 sayısı bir integer mi", isinstance(5, int))
print("merhaba bir string mi", isinstance("merhaba", str))

# 8- dir(): Bir nesnenin kullanılabilir metot ve özelliklerini listeler.
print("integer ==>",dir(int))
print("string ==>",dir(str))

# 9- local, global
# globals(): Global değişkenlerin sözlüğünü döndürür.
# locals():  Yerel değişkenlerin sözlüğünü döndürür.
glo=10
def glo_function():
    loca=20
    print("Local function: ", locals())
    print("Global function: ", globals())
glo_function()