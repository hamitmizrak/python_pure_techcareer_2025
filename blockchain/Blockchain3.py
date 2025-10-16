# import
from typing import List  # List type
import time  # Blok zaman damgası için kullandım
import json  # Blok verilerini JSON formatında saklamak istersek
import hashlib  # Hash fonksiyonlarını kullanmak içindir.
from colorama import Fore, Style # Terminalde renkli çıktı almak için
from datetime import datetime  # Zamanı okunabilir hale getirmek için

################################
# Fonksiyonlar
class Block:
    """
    Blockchain içindeki her bir bloğu temsil eden sınıf.
    """

    def __init__(self, index: int, previous_hash: str, transactions: List[dict], nonce: int = 0):
        """
        Bir blok nesnesi oluşturur.

        :param index: Blok zinciri içindeki sıra numarası (0'dan başlar).
        :param previous_hash: Önceki bloğun SHA-256 hash değeri.
        :param transactions: Blok içinde saklanan işlem listesi.
        :param nonce: Madencilik sürecinde kullanılan sayısal değer (başlangıç değeri 0).
        """
        self.index = index  # Blok numarası
        self.timestamp = time.time()  # Blok oluşturulma zamanı (Unix zaman damgası olarak saklanır)
        self.previous_hash = previous_hash  # Önceki bloğun hash değeri
        self.transactions = transactions  # Blok içindeki işlemler
        self.nonce = nonce  # Proof of Work için kullanılan nonce değeri
        self.hash = self.calculate_hash()  # Blok için hash değeri hesaplanır

    def calculate_hash(self):
        """Blok verilerini SHA-256 algoritması kullanarak hash'ler."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_readable_timestamp(self):
        """Timestamp değerini okunabilir hale getirir."""
        return datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')


class Blockchain:
    """
    Blockchain yapısını yöneten sınıf.
    """

    def __init__(self):
        self.chain: List[Block] = []  # Blockchain zinciri (blokları saklar)
        self.pending_transactions: List[dict] = []  # İşlem havuzunda bekleyen işlemler
        self.difficulty = 4  # Madencilik zorluk seviyesi (başlangıç olarak 4 sıfır)
        self.create_genesis_block()  # İlk bloğu oluştur

    def create_genesis_block(self):
        """Blockchain'in ilk bloğunu (Genesis Block) oluşturur."""
        genesis_block = Block(index=0, previous_hash="0", transactions=[], nonce=0)
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, recipient: str, amount: float):
        """Yeni bir işlem oluşturup bekleyen işlemler listesine ekler."""
        self.pending_transactions.append({
            "sender": sender, # Kim gönderiyor ?
            "recipient": recipient, # Kime gönderiyor ?
            "amount": amount # Ne kadar gönderiyor ?
        })

        # 3 işlem eklendikten sonra otomatik madencilik
        if len(self.pending_transactions) >= 3:
            self.mine_block()

    def mine_block(self):
        """Yeni bir blok üretmek için madencilik işlemini gerçekleştirir."""
        if not self.pending_transactions:
            print(Fore.RED + "İşlem kuyruğu boş, madencilik yapılacak işlem yok." + Style.RESET_ALL)
            return None

        last_block = self.chain[-1]
        new_block = Block(index=len(self.chain), previous_hash=last_block.hash, transactions=self.pending_transactions,
                          nonce=0)

        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        print(Fore.GREEN + f"Yeni blok madenciliği tamamlandı: {new_block.hash}" + Style.RESET_ALL)
        self.chain.append(new_block)
        self.pending_transactions = []

    def is_chain_valid(self):
        """Blockchain'in bütünlüğünü doğrulayan fonksiyon."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        """Blockchain içeriğini ekrana yazdıran fonksiyon."""
        for block in self.chain:
            print(
                Fore.CYAN + f"Blok {block.index} - Zaman: {block.get_readable_timestamp()} - Hash: {block.hash} - Önceki Hash: {block.previous_hash}" + Style.RESET_ALL)

    def get_balance(self, user: str):
        """Belirli bir kullanıcının bakiyesini hesaplar."""
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["sender"] == user:
                    balance -= transaction["amount"]
                if transaction["recipient"] == user:
                    balance += transaction["amount"]
        return balance

    def export_to_json(self):
        """Blockchain verisini JSON formatında dışa aktarır."""
        return json.dumps([block.__dict__ for block in self.chain], indent=4)

# Blockchain üretimi
my_blockchain = Blockchain()

# Hamit'ten Mehmet'e 10 birim gönderme ekle
my_blockchain.add_transaction("Hamit", "Mehmet", 10)

# Ahmet'ten Mustafa'ya 15 birim gönderme ekle
my_blockchain.add_transaction("Mehmet", "Mustafa", 5)

# İşlemleri içeren yeni bir blok madenciliğini yap ve ekle
# test_chain.mine_block()

# Fatih'ten Sultan'a 10 birim gönderme ekle
my_blockchain.add_transaction("Mustafa", "Fatih", 2)
# test_chain.mine_block()

# Blockchainleri ekrana yazdır
my_blockchain.print_chain()

print(Fore.BLUE + "Hamit'in bakiyesi:", my_blockchain.get_balance("Hamit"), Style.RESET_ALL)
print(Fore.BLUE + "Mehmet'in bakiyesi:", my_blockchain.get_balance("Mehmet"), Style.RESET_ALL)
print(Fore.BLUE + "Mustafa'in bakiyesi:", my_blockchain.get_balance("Mustafa"), Style.RESET_ALL)
print(Fore.BLUE + "Fatih'in bakiyesi:", my_blockchain.get_balance("Fatih"), Style.RESET_ALL)

# İşlem kuyruğu boş, madencilik yapılacak işlem yok.
my_blockchain.mine_block();

# Blockchain bütünlük doğrulaması
print(Fore.YELLOW +"Blokchain geçerli mi? ", my_blockchain.is_chain_valid(), Style.RESET_ALL)

# Blockchain'i JSON olarak dışa aktarma
print(Fore.MAGENTA + "Blockchain JSON Formatı:")
print(my_blockchain.export_to_json())

