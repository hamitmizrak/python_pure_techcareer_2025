# pip --version


"""
PAD-UNPAD AES,DES şifreleme algoritmalarında kulllanılır:
Şifrelemede öncesinde PAD
Şifre çözümlemede UNPAD

pad, unpad bu fonksiyonlar AES,DES blok şifrelemede algoritmalarında
veriyi istediğimizi formda kullanmak için bu fonksiyonunu çağırız.

1-pad: Doldurma: veriyi belirli bir blok boyutuna tamamlamak içindir
Sabit blok şifrelme algoritmalarıya çalışırız örneğin: 16 byte Eüer veriyi tam blok haline getirmezseni şifreleme çalışmaz.

2-unpad: Kaldırma: şifrelenmiş verinin tamamına ulaşana kadar bırakılan paddingı kaldırır.
pad tarafından eklenen fazlalıkları kaldırarak veriyi original haline getirmek
"""

"""
HASHING (Özetleme): Tekyönlü geri dönüşü mümkün değil
Herhangi bir veriyi sabit uzunlukta özet değerine dönüştüren amtematiksel fonksiyonlardır.
NOT: Hash fonksiyonları şifreleme değildirrrrrrrr. sadece ama sadece veri özetleme yapısıdır.
Anahtar kullanılmaz, sabit uzunlukta özet üretir.
Hızlı, SHA-2, BLAKE2 modern algoritmalar

Yaygın Hash Algoritmaları
MD5, SHA-1, SHA-256, SHA-512, BLAKE2/ARgon2: Parola saklama ve modern güvenlik ihtiyaçlarını karşılır. 


Kullanım alanları
Parola saklama
dosya bütünkük kontrolü
Blockchain teknolojisinde 
digital imzalarda
"""

########################################################################
import hashlib
from colorama import Fore, Style # Renkli çıktı için

########################################################################
# Renkler için kısayollar
RED= Fore.RED
GREEN= Fore.GREEN
YELLOW= Fore.YELLOW
BLUE= Fore.BLUE
MAGENTA= Fore.MAGENTA
CYAN= Fore.CYAN
WHITE= Fore.WHITE
RESET=Style.RESET_ALL # Renk sıfırlamak

########################################################################
# Hashing (Örnek: e-posta adresi)
data = "hamitmizrak@gmail.com:1234567".encode() # string veriyi byte formanıta çevir


########################################################################
# MD5 Hash algoritmasını kullanarak verinin hash değerini hesaplayalım
# 32 hex karakter (0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f)  32^16
md5_hash = hashlib.md5(data).hexdigest()
print(f"{BLUE}MD5 Hash:\t\t {RESET} ", md5_hash,"\n")


########################################################################
# SHA-256 Hash algoritmasını kullanarak verinin hash değerini hesaplayalım
# 64 hex karakter (0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f)  64^16
sha256_hash = hashlib.sha256(data).hexdigest()
print(f"{CYAN}SHA-256:\t\t {RESET} ", sha256_hash,"\n")

########################################################################
# Blake2 Hash algoritmasını kullanarak verinin hash değerini hesaplayalım
# 128 hex karakter (0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f)  128^16
blake2b_hash = hashlib.blake2b(data).hexdigest()
print(f"{YELLOW}blake2 Hash:\t {RESET} ", blake2b_hash,"\n")