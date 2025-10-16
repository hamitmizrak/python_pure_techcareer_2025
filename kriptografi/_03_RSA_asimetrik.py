# pip --version
# pip install pycryptodo    # AES kütüphanesi
# pip install colorama      # Color

# Eğer paket yüklenmezse
# pip uninstall pycryptodo
# pip install pycryptodo --no-cache-dir

# BC (Cipher Block Chaining)
# Simetrik: Aynı anahtar hem şifreleme hemde çözme işlemleri için kullanılır.
# Asimetrik: İki farklı anahtar kullanılır(public,private)

# 3. RSA (Rivest Shamir Adleman) - Asimetrik Şifreleme
# 8 bit= 1 Bayt

"""
AES,DES şifreleme algoritmalarında kulllanılır:
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
RSA (Rivest Shamir Adleman) Asimetrik:
1977 yılında geliştirilmiştir
İki farklı anahtar (public,private) kullanılır.
Anahtar uzunluğu: 1024-bit, 2048-bit, 4096-bit kullanılır ancak biz genelde 2048-bit kullanılır.
AES,DES'e göre çok daha yavaştır.

SSL/TLS (HTTPS)
Digital imza
Kripto para cüzdanlarında

Anahtar üretim: Büyük asal sayılar kullanılır. 2,3,5,7,11,13,17,19,23 ...
public key: Veriyi şifrelemek
private key: Veriyi çözmek için gereken anahtar
"""

########################################################################
from Crypto.PublicKey import RSA         # RSA şifreleme kütüphanesi
from Crypto.Cipher import PKCS1_OAEP    #
# import os # Rastgelere anahtar üretmek için kullanılan kütüphanesi
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
#  8 bit = 1 byte
# RSA Anahtar ürütmek
# key = os.urandom(8) # 256-bit DES anahtarı güvenli ve rastgele için (2.YOL) AES
# key = b"8bytkey1" # 8 bayt uzunluğunda bir anahtar (1.YOL) DES
key = RSA.generate(2048) # 2048-bit RSA anahtarı üret
public_key = key.publickey().export_key()
private_key = key.export_key()

print(f"{YELLOW}Genel Anahtar (RSA): ", public_key.decode()+"\n\n")
print(f"{RED}Özel Anahtar (RSA): ", private_key.decode()+"\n\n")


# Şifrelenecek veriyi tamamladık (Örnek: e-posta adresi)
data = "hamitmizrak@gmail.com:1234567".encode() # string veriyi byte formanıta çevir

#
rsa_public_key =RSA.import_key(public_key)

# Şifreleme (Public Key)
cipher = PKCS1_OAEP.new(rsa_public_key) # DES nesnesini oluştur (CBC modu ve IV)


# Veriyi AES şifreleme bloğu boyutuna uygun hale getirmek için pad() kullanılıyoruz.
# AES blok boyutu 16 byte olduğu için eksik kalan kısımları uygun bir şemada dolduralım.
ciphertext= cipher.encrypt(data)

# Şifrelenmiş verileri hexadecimal formatında ekrana yazdırıyoruz.
# print(f"{BLUE}Şifrelenmiş Veri (AES, CBC Modu): {RESET}{ciphertext.hex()} ")
print(f"{CYAN}Şifrelenmiş Veri (RSA): {RESET} ", ciphertext.hex()+"\n")

# RSA şifre çözme (private key)
rsa_private_key = RSA.import_key(private_key)
decipher= PKCS1_OAEP.new(rsa_private_key)
decrypted_data= decipher.decrypt(ciphertext)

# Şifre çözülmüş verileri ekrana yazdırıyoruz.
print(f"{CYAN}Çözülmüş ilk veri: (RSA): {RESET} ", decrypted_data.decode())
