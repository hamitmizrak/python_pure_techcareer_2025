# pip --version
# pip install pycryptodo    # AES kütüphanesi
# pip install colorama      # Color

# Eğer paket yüklenmezse
# pip uninstall pycryptodo
# pip install pycryptodo --no-cache-dir

# BC (Cipher Block Chaining)
# Simetrik: Aynı anahtar hem şifreleme hemde çözme işlemleri için kullanılır.
# Asimetrik: İki farklı anahtar kullanılır(public,private)

# 1. AES (Advanced Encryption Standard) - Simetrik Şifreleme
# AES için Python'da pycryptodome kütüphanesini kullanabiliriz.
# AES, 128-bit blok boyutunda çalışır ve CBC (Cipher Block Chaining) gibi modlarla güvenliği artırabiliriz.

# 8bit=1Bayt

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
AES: Simetrik
AES, simetrik anahtarlı blok şifreleme algoritmasıdır.
2001 yılında NIST (National Instute of Standards and Technology)
Rijndael algorithm dayanır
128-bit, 192-bit, 256-bit
Günümüz şarlarında DES'e göre daha güvenlidir.
Yüksek Hız verimliliği, güçlü, brute force saldırılarına dayanıklıdır.
Veri şifreleme
WPA2,WPA3
VPN
"""

########################################################################
from Crypto.Cipher import AES    # AES şifreleme kütüphanesi
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
# AES için 256-bit(32 byte) uzunluğunda rastgele bir anahtar oluştur
key = os.urandom(32) # 256-bit AES anahtarı güvenli ve rastgele için

# AES için initialization Vector(IV) olarak 16 byte olarak rastgele bir değer oluştur
iv= os.urandom(16)   # AES için Initialization Vector

# Şifrelencek veriyi tamamladık (Örnek: e-posta adresi)
data = "hamitmizrak@gmail.com:123456".encode() # string veriyi byte formanıta çevir

# AES şifreleme (CBC Modu)
cipher = AES.new(key, AES.MODE_CBC,iv) # AES nesnesini oluştur (CBC modu ve IV)

# Veriyi AES şifreleme bloğu boyutuna uygun hale getirmek için pad() kullanılıyoruz.
# AES blok boyutu 16 byte olduğu için eksik kalan kısımları uygun bir şemada dolduralım.
ciphertext= cipher.encrypt(pad(data, AES.block_size))

# Şifrelenmiş verileri hexadecimal formatında ekrana yazdırıyoruz.
print(f"{CYAN}AES:İlk Veri şifrelenmeden önce): {RESET} {data.decode()}  ", data)
# print(f"{BLUE}Şifrelenmiş Veri (AES, CBC Modu): {RESET}{ciphertext.hex()} ")
print(f"{BLUE}Şifrelenmiş Veri (AES, CBC Modu): {RESET} ", ciphertext.hex())

# AES şifre çözme (CBC Modu)
# AES şifre çözme işlemi için aynı anahtar ve IV ile yeni bir AES nesnesi oluşturuyoruz.
decipher = AES.new(key, AES.MODE_CBC, iv)

# Şifrelenmiş verileri AES şifre çözme bloğuna uygun hale getirmek için unpad() kullanıyoruz.
decipher_data= unpad(decipher.decrypt(ciphertext), AES.block_size)

# Şifre çözülmüş verileri ekrana yazdırıyoruz.
print(f"{RED}Çözülmüş ilk veri: (AES): {RESET} ", decipher_data.decode())
