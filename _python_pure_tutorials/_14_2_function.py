################################################################################
#### Function   ################################################################

# parametre  default değer
def hesap_topla5(sayi1,sayi2=20):
    """docstring
    Bu function Parametreli Returlu toplama yapar
    """
    sayi3=sayi1+sayi2
    return sayi3

# Fuction calling
# result5=hesap_topla5(10)
# print(f"{result5}")
#
# result5=hesap_topla5(10,40)
# print(f"{result5}")

################################################################################
#### Function beartype #########################################################
# Tür ihlali -> TypeError
from beartype import beartype

# 1.YOL
# python -m pip install beartype  ==> Windows (Uzun Hali)
# py -m pip install beartype      ==> Windows (Kısaltma)
# pip3  install beartype          ==> Mac || Linux

# 2.YOL
# cat requirements44.txt
# pip install -r requirements44.txt

# int, float, NoneType, str, bool, list, tuple, set, dict  ==> hint types

@beartype
def hesap_topla6(sayi1:int=0,sayi2:int=0) -> int:
    return sayi1+sayi2

print(f"{hesap_topla6()}")
print(f"{hesap_topla6(3)}")
print(f"{hesap_topla6(3,6)}")
# print(f"{hesap_topla6(3,"6")}")


################################################################################
#### (for veya while), break, continue, pass ###################################
# step-1) kullanıcı tarafından başlangıç ve bitiş sayıları verilsin
# step-2) Başlangıç ile bitiş sayıları arasında sayıların toplamını yapınız ?
# step-3) Eğer sayı eğer 10 sonra devam ediyorsa dur (döngüyü bitir) ?
# step-4) Eğer bu döngüdeki sayılarda 5 varsa işleme alma(toplama yapma) ?
# step-5) Eğer bu döngüdeki sayılarda 6 varsa bir şey yapma (pass'ı ekleyiniz) ?
# step-6) 1-10 arasındaki tek sayıları gösteriniz ve tek sayıları toplayınız ?
# step-7) 1-10 arasındaki çift sayıları gösteriniz ve çift sayıları toplayınız ?