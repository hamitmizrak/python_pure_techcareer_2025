################################################################################
#### Conditional ###############################################################

# Sayı Negatif mi, Pozitif mi ?
# if else
number:int=44
if number > 0:
    print(f"Pozitif sayı")
else:
    print(f"Negatif sayı")

# Ternary
ternary:int ="Pozitif sayı" if number > 0 else "Negatif sayı"
print(f"{ternary}")

# if elif else
number_data:int=5
if number_data==1:
    print(f"Sayı bir")
elif number_data==2:
    print(f"Sayı iki")
elif number_data==3:
    print(f"Sayı üç")
elif number_data==4:
    print(f"Sayı dört")
elif number_data==5:
    print(f"Sayı beş")
else:
    print("1<=Sayı<=5 bunların dışında")


# İç içe if
number_content:int=+15
if number_content > 0:
    print(f"Pozitif => ",end="")
    if number_content % 2 ==0:
        print(" Çift sayı")
    else:
        print(number_content, f"Tek sayı")
else:
    print(f"Negatif sayı")

# pass : Koşul bloklarında geçici olarak bir data  verilerini yapmamak için "pass" kullanırız
number_input= int(input("Lütfen bir sayı giriniz"))
if number_input > 0:
    print(f"Pozitif => ",end="")
    if number_content % 2 ==0:
        print(" Çift sayı")
        if number_content %3==1:
            pass # Daha sonrasında buraya kod eklenecek
    else:
        print(number_content, f"Tek sayı")
else:
    print(f"Negatif sayı")
