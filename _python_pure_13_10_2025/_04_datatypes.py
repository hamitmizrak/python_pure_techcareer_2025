
# Dynamics Types
# Değişken isimlendirme ==> kullanalım (_ ) yani  (yani snake_case)
#

#################################################################################
####### sayılar (Number)#########################################################
# Number (Pozitif sayılar)
number1 = 10   # Tam sayılar ==> (Pozitif)
number2 = +10  # Tam sayılar ==> (Pozitif)
number3 = -10  # Tam sayılar ==> (Negatif)
PI=3.14159     # Tam sayılar ==> (Virgüllü)
print(f"number1:{number1}  number2:{number2} number3:{number3} ")

#################################################################################
####### types ###################################################################
# types: Verinin türünü öğrenmek istiyorsak
print(f"number1:{number1}  ==> Türü: {type(number1)}")


#################################################################################
####### string###################################################################
# string: Verinin dizgi (kelime)
name="Hamit"
surname="Mızrak"
print(f"Adım:  {name}  Soyadım:  {surname}")   # string => kelime

#################################################################################
####### boolean #################################################################
# Boolean: bir şey ya doğrudur(True) yada yanlıştır(False)
is_login= True
print(f"Login mi ? {is_login} ==> Türü: {type(is_login)}" )