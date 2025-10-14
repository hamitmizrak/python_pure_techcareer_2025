# Dynamics Types
# Değişken isimlendirme ==> kullanalım (_ ) yani  (yani snake_case)

# 1.YOL ==> Normal değişken türü
data1=1
data2=2
data3=3
print(data1,data2,data3)

# 2.YOL ==> Değişekneleri tek satırda göstermek
data4,data5,data6=44,55,66
print(data4,data5,data6)

#################################################################################
####### Data Types ##############################################################
# Data Types
number1 = 10   # Tam sayılar ==> (Pozitif)
number2 = +10  # Tam sayılar ==> (Pozitif)
number3 = -10  # Tam sayılar ==> (Negatif)
PI=3.14159     # Tam sayılar ==> (Virgüllü)
name="Hamit"   # string
is_login= True # boolean
my_list  = [1,2,3,4,5, "Malatya", 14.53, True, False]  # list
my_tuple = (1,2,3,4,5, "Malatya", 14.53, True, False)  # tuple => değiştirilemez(immutable)
my_set   = {1,1,1,1,2,3,4,5, "Malatya", 14.53, True, False}  # set => benzersiz eleman(unique)
my_dictionary ={
    "name":"Hamit",
    "surname":"Mızrak",
    "is_login":True
}

# 8 tane tür
# int, float, str, bool, list, tuple, set, dict
#################################################################################
####### int (Number) #############################################################
# types: Verinin türünü öğrenmek istiyorsak
# number türü ==> int
print(f"number1:{number1}  number2:{number2} number3:{number3} ")
print(f"number1:{number1}  ==> Türü: {type(number1)}")

#################################################################################
####### float (Number) #############################################################
# types: Verinin türünü öğrenmek istiyorsak
# number türü ==> float
print(f"PI:{PI}  ==> Türü: {type(PI)}")

#################################################################################
####### string###################################################################
# string: Verinin dizgi (kelime)
# string türü ==> str
print(f"Adım:{name}  ==> Türü:  {type(name)}")   # string => kelime

#################################################################################
####### boolean #################################################################
# Boolean: bir şey ya doğrudur(True) yada yanlıştır(False)
# bool türü ==> bool
print(f"Login mi ? {is_login} ==> Türü: {type(is_login)}" )


#################################################################################
####### List ####################################################################
# List: Birden fazla veriyi hafızada tutmak için
# List türü ==> list
print(f"listem ==> {my_list}, Types => {type(my_list)}")


#################################################################################
####### Tuple(Demet) ############################################################
# Tuple: Liste yapısına çok benzer ancak buradaki değerler değiştirilemez(immutable)
print(f"tuple(immutable) => {my_tuple}, Types => {type(my_tuple)}")


#################################################################################
####### Set(Benzersiz) ##########################################################
# Set: Her elemanın benzersiz olduğunu göstermek için
# True==1,  False==0 , eğer elemanlarda 1 varsa True demektir zaten
print(f"set(unique) => {my_set}, Types => {type(my_set)}")


#################################################################################
####### Dictionary(Kütüphane) ###################################################
# Dictionary: Değer çiftlerin <Key,Value> olarak hafızada tutmak
print(f"Dictionary(OOP) => {my_dictionary}, Types => {type(my_dictionary)}")
