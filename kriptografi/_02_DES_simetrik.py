# pip --version
# pip install pycryptodo    # AES kütüphanesi
# pip install colorama      # Color

# Eğer paket yüklenmezse
# pip uninstall pycryptodo
# pip install pycryptodo --no-cache-dir

# BC (Cipher Block Chaining)
# Simetrik: Aynı anahtar hem şifreleme hemde çözme işlemleri için kullanılır.
# Asimetrik: İki farklı anahtar kullanılır(public,private)

# 2. DES (Data Encryption Standard) - Simetrik Şifreleme
# 8 bit = 1 Bayt


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
DES: Simetrik
IBM tarafından 1977 NIST NIST (National Instute of Standards and Technology)
Simetrik blok şifreleme
Günümüzde güvenlik açısından çokta tercih edilmiyor.
Anahtar uzunluğu: 56-bit
Blok boyutu: 64-bit
Düşük Hız, güçlü, brute force saldırılarına dayanıksız.
ATM pin şifreleme
Eski güvenlik sistemlerinde
"""

########################################################################
from Crypto.Cipher import DES    # AES şifreleme kütüphanesi
from Crypto.Util.Padding import pad,unpad # Veri bloklarını tamamlama ve kaldırma fonksiyonu
import os # Rastgelere anahtar üretmek için kullanılan kütüphanesi
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
# DES için 8 byte(8*8=64 bit) anahtar uzunluğunda
# key = os.urandom(8) # 256-bit DES anahtarı güvenli ve rastgele için (2.YOL)
key = b"8bytkey1" # 8 bayt uzunluğunda bir anahtar (1.YOL)


# DES için  8 byte olarak rastgele bir değer oluştur
iv= os.urandom(8)   # DES için Initialization Vector


# Şifrelencek veriyi tamamladık (Örnek: e-posta adresi)
data = "hamitmizrak@gmail.com:1234567".encode() # string veriyi byte formanıta çevir

# AES şifreleme (CBC Modu)
cipher = DES.new(key, DES.MODE_CBC,iv) # DES nesnesini oluştur (CBC modu ve IV)

# Veriyi AES şifreleme bloğu boyutuna uygun hale getirmek için pad() kullanılıyoruz.
# AES blok boyutu 16 byte olduğu için eksik kalan kısımları uygun bir şemada dolduralım.
ciphertext= cipher.encrypt(pad(data, DES.block_size))

# Şifrelenmiş verileri hexadecimal formatında ekrana yazdırıyoruz.
print(f"{CYAN}AES:İlk Veri şifrelenmeden önce): {RESET} {data.decode()}  ", data)
# print(f"{BLUE}Şifrelenmiş Veri (AES, CBC Modu): {RESET}{ciphertext.hex()} ")
print(f"{BLUE}Şifrelenmiş Veri (AES, CBC Modu): {RESET} ", ciphertext.hex())

# AES şifre çözme (CBC Modu)
# AES şifre çözme işlemi için aynı anahtar ve IV ile yeni bir AES nesnesi oluşturuyoruz.
decipher = DES.new(key, DES.MODE_CBC, iv)

# Şifrelenmiş verileri AES şifre çözme bloğuna uygun hale getirmek için unpad() kullanıyoruz.
decipher_data= unpad(decipher.decrypt(ciphertext), DES.block_size)

# Şifre çözülmüş verileri ekrana yazdırıyoruz.
print(f"{RED}Çözülmüş ilk veri: (AES): {RESET} ", decipher_data.decode())
