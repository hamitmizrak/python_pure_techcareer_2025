import hashlib  # Hash fonksiyonlarını kullanmak için
import json  # Blok verilerini JSON formatında saklamak için
import time  # Blok zaman damgası için
from typing import List  # Tip belirtimi için


class Block:
    """
    Blockchain içindeki her bir bloğu temsil eden sınıf.
    """

    def __init__(self, index: int, previous_hash: str, transactions: List[dict], nonce: int = 0):
        self.index = index  # Blok numarası
        self.timestamp = time.time()  # Blok oluşturulma zamanı
        self.previous_hash = previous_hash  # Önceki bloğun hash değeri
        self.transactions = transactions  # Blok içindeki işlemler
        self.nonce = nonce  # Madencilik için kullanılan nonce değeri
        self.hash = self.calculate_hash()  # Blok için hash değeri hesapla

    def calculate_hash(self):
        """Blok verilerini kullanarak hash hesaplayan fonksiyon."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()  # SHA-256 hash üretimi


class Blockchain:
    """
    Blockchain yapısını yöneten sınıf.
    """

    def __init__(self):
        self.chain: List[Block] = []  # Blockchain zinciri
        self.pending_transactions: List[dict] = []  # Bekleyen işlemler listesi
        self.difficulty = 4  # Proof of Work madencilik zorluk seviyesi
        self.create_genesis_block()  # İlk bloğu oluştur

    def create_genesis_block(self):
        """Blockchain'in ilk (genesis) bloğunu oluşturur."""
        genesis_block = Block(index=0, previous_hash="0", transactions=[], nonce=0)
        self.chain.append(genesis_block)  # Genesis bloğunu zincire ekler

    def add_transaction(self, sender: str, recipient: str, amount: float):
        """Yeni bir işlem ekleyen fonksiyon."""
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

    def mine_block(self):
        """Yeni bir blok madenciliği yaparak blockchain’e ekler."""
        if not self.pending_transactions:
            print("İşlem kuyruğu boş, madencilik yapılacak işlem yok.")
            return None

        last_block = self.chain[-1]  # Zincirin en son bloğunu al
        new_block = Block(index=len(self.chain), previous_hash=last_block.hash, transactions=self.pending_transactions,
                          nonce=0)

        # Proof of Work - Belirli sayıda sıfır ile başlayan hash bulana kadar nonce artır
        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        print(f"Yeni blok madenciliği tamamlandı: {new_block.hash}")
        self.chain.append(new_block)  # Yeni bloğu blockchain'e ekle
        self.pending_transactions = []  # İşlem listesini sıfırla

    def is_chain_valid(self):
        """Blockchain'in bütünlüğünü doğrular."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False  # Hash eşleşmiyorsa, blockchain geçersizdir
            if current_block.previous_hash != previous_block.hash:
                return False  # Önceki bloğun hash değeri yanlışsa, blockchain geçersizdir

        return True

    def print_chain(self):
        """Blockchain’i ekrana yazdırır."""
        for block in self.chain:
            print(f"Blok {block.index} - Hash: {block.hash} - Önceki Hash: {block.previous_hash}")


# Blockchain Kullanımı
# Yeni bir blockchain oluştur
test_chain = Blockchain()
test_chain.add_transaction("Hamit", "Mehmet", 10)  # Alice'den Bob'a 10 birim gönderme işlemi ekle
test_chain.add_transaction("Mehmet", "Ali", 5)  # Bob'dan Charlie'ye 5 birim gönderme işlemi ekle

test_chain.mine_block()  # İşlemleri içeren yeni bir blok madenciliği yap ve ekle

test_chain.add_transaction("Ali", "Mustafaya", 2)  # Charlie'den Alice'e 2 birim gönderme işlemi ekle
test_chain.mine_block()  # Yeni blok madenciliği yap ve ekle

# Blockchain doğrulaması
test_chain.print_chain()  # Blockchain'i ekrana yazdır
print("Blockchain geçerli mi?:", test_chain.is_chain_valid())  # Blockchain bütünlüğünü doğrula
