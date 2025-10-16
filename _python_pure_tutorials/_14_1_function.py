################################################################################
#### Function   ################################################################

#### Function (Parametresiz, Retursuz) ########################################
# 1-) Function => Parametresiz, Retursuz
def hesap_topla1():
    """docstring
    Bu function parametresiz retursuz toplama yapar
    """
    sayi1=10
    sayi2=20
    sayi3=sayi1+sayi2
    print(f"{sayi1} + {sayi2} = {sayi3}")

# Fuction calling
hesap_topla1()



#### Function (Parametreli, Retursuz) ########################################
# 2-) Function => Parametreli, Retursuz
def hesap_topla2(sayi1,sayi2):
    """docstring
    Bu function parametreli retursuz toplama yapar
    """
    sayi3=sayi1+sayi2
    print(f"{sayi1} + {sayi2} = {sayi3}")

# Fuction calling
hesap_topla2(10,20)

#### Function (Parametresiz, Returnlu) ########################################
# 3-) Function => Parametresiz, Returlu
def hesap_topla4():
    """docstring
    Bu function parametresiz Returnlu toplama yapar
    """
    sayi1 = 10
    sayi2 = 20
    sayi3=sayi1+sayi2
    return sayi3


# Fuction calling
result3 =hesap_topla4()
print(f"{result3}")


#### Function (Parametreli, Returlu) ########################################
# 4-) Function => Parametreli, Retursuz
def hesap_topla4(sayi1,sayi2):
    """docstring
    Bu function Parametreli Returlu toplama yapar
    """
    sayi3=sayi1+sayi2
    return sayi3

# Fuction calling
result4=hesap_topla4(10,20)
print(f"{result4}")

################################################################################
#### (for veya while), break, continue, pass ###################################
# step-1) kullanıcı tarafından başlangıç ve bitiş sayıları verilsin
# step-2) Başlangıç ile bitiş sayıları arasında sayıların toplamını yapınız ?
# step-3) Eğer sayı eğer 10 sonra devam ediyorsa dur (döngüyü bitir) ?
# step-4) Eğer bu döngüdeki sayılarda 5 varsa işleme alma(toplama yapma) ?
# step-5) Eğer bu döngüdeki sayılarda 6 varsa bir şey yapma (pass'ı ekleyiniz) ?
# step-6) 1-10 arasındaki tek sayıları gösteriniz ve tek sayıları toplayınız ?
# step-7) 1-10 arasındaki çift sayıları gösteriniz ve çift sayıları toplayınız ?