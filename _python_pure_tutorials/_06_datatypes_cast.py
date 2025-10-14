# int, float, NoneType, str, bool, list, tuple, set, dict

# Cast: Type Casting yani veri türlerinin birbirine dönüştürülmesine denir

# int()        ==> Tam sayıya çevir
# float()      ==> Virgüllü sayıya çevir
# str()        ==> Kelime çevir
# bool()        ==> Kelime çevir

number1="44"
print(f"{number1} => type {type(number1)}")
print(f"{number1} => type {int(number1)+16}")


number1=int(number1);
print(f"{number1} => type {type(number1)}")

number1=float(number1);
print(f"{number1} => type {type(number1)}")