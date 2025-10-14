"""
1-) Aritmetik Operators
    a) Toplama: +
    b) Çıkarma: -
    c) Çarpma: *
    d) Bölme: /
    e) Mod: %
    f) Üs Alma: **
    g) Kalan Sayı Bulma: //


2-) Atama Operators
    a) Atama: =
    b) Artı Eşittir: +=
    c) Çıkar Eşittir: -=
    d) Bölme Eşittir: /=
    e) Mod Eşittir: %=
    f) Üs Alma Eşittir: **=
    g) Kalan Sayı Bulma Eşittir: //=

3-) Karşılaştırma Operators
    a) Eşittir: ==
    b) Eşit Değil:  !=
    c) Büyük Eşittir: >=
    d) Büyük Değil: <=
    e) Küçük Eşittir: <

4-) Mantıksal Operators
    a) VEYA: or   => ||
    b) VE: and    => &&
    c) Değil: not => !

5-) Bit Düzeyinde (Bitwise) Operators  (Bit Düzeyinde: 0 ve 1 olanlardır)
    a) Bitwise AND: &
    b) Bitwise OR: |
    c) Bitwise XOR: ^
    d) Bitwise NOT: ~
    e) Bitwise Left Shift: <<
    f) Bitwise Right Shift: >>
    g) Bitwise Right Shift (unsigned): >>


5-) Atanma ve İfadeler
    a) İfadeleri Birleştirir: +, -, *, /, %, **, //, ==,!=, >, <, >=, <=, or, and, not
    b) Atama İfadesi: =, +=, -=, *=, /=, %=, **=, //=
    c) İfadeleri Öncelik Belirlemek için Parantezler: ()
    d) İfadeleri Birleştirirken İç içe kullanmak için Parantezler: ()
    e) İfadeleri Birleştirirken Boşluklarla veya İfadeler arasında Boşluklar: ()
    f) İfadeleri Birleştirirken İfadeler arasında ��arpanlar: ()
    g) İfadeleri Birleştirirken İfadeler arasında Kullanılan Operatörler: +, -, *, /, %, **, //, ==,!=, >, <, >=, <=, or, and, not

6-) Üyelik Operatör
    a) İçinde İçe Kullanılan İfadeler    : in
    b) İçinde İçe Kullanılmamış İfadeler : not in
    c) İçinde İçe Kullanılan İfadeler    : is

7-) Kimlik Operators
    a) Kopyalanan İfadeler: =
"""

######################################################################################
####### Sayısal İşlemler(+-*/% **) ###################################################
number1,number2=15,4


print(f"toplama= {number1+number2}")   # 1.YOL
#print(f"1.sayı={number1} + 2.sayı={number2} toplama= {number1+number2}")   # 1.YOL
#print("toplama: ",(number1+number2))  # 2.YOL

print(f"Çıkarma= {number1-number2}")
print(f"Çarpma=  {number1*number2}")
print(f"Bölme=   {number1/number2}")
print(f"Kalan=   {number1%number2}")
print(f"üslü=    {number1**number2}")  # **

######################################################################################
####### Sayısal İşlemler Logic #######################################################
print(f"Eşit       mi ? {number1==number2}")
print(f"Eşit değil mi ? {number1!=number2}")

print(f"Büyük mü ? {number1>number2}")
print(f"Büyük veya Eşitmi mü ? {number1>=number2}")

print(f"Küçük mü ? {number1>number2}")
print(f"Küçük veya Eşitmi mü ? {number1<=number2}\n")

######################################################################################
####### Sayısal İşlemler Logic #######################################################
number3=11; # Noktalı virgül yazmak bir şeyi değiştirmez
print(f"number => {number3}")

# 1.YOL
number3=number3+1;
print(f"number => {number3}")

# 2.YOL
number3+=1;
print(f"number => {number3}")