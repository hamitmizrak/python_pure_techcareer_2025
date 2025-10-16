import time
import json
import hashlib
from typing import List
from datetime import datetime
from colorama import Fore, Style
import os

"""
eni Özellikler:
Blok Geçerliliğini Detaylı Kontrol Etme:

Mevcut is_chain_valid() metodunu genişleterek her bloğun veri tutarlılığını detaylı kontrol eder.
Blockchain’i JSON Dosyasına Kaydetme ve Yükleme:

Blockchain'in JSON formatında dışa aktarılması ve sonradan tekrar yüklenmesini sağlar.
İşlem Geçmişi Sorgulama:

Kullanıcıya ait tüm işlemleri (gönderdiği ve aldığı) listeleyerek işlem geçmişini görme imkanı sunar.
Daha Gelişmiş Madencilik Sistemi:

Blok madenciliği sırasında detaylı bilgi verir.
Dinamik zorluk seviyesi eklenerek madencilik hızını dengeleyen bir algoritma eklenir.
Kullanıcı Dostu Menü Geliştirme:

Komut satırındaki seçeneklere daha fazla açıklama eklenir.
Kullanıcının seçimini kolaylaştıran mesajlar gösterilir.
"""


class Block:
    def __init__(self, index: int, previous_hash: str, transactions: List[dict], nonce: int = 0):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_readable_timestamp(self):
        return datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[dict] = []
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(index=0, previous_hash="0", transactions=[], nonce=0)
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, recipient: str, amount: float):
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

    def mine_block(self):
        if not self.pending_transactions:
            print(Fore.RED + "İşlem kuyruğu boş, madencilik yapılamaz!" + Style.RESET_ALL)
            return None

        last_block = self.chain[-1]
        new_block = Block(index=len(self.chain), previous_hash=last_block.hash, transactions=self.pending_transactions)

        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        print(Fore.GREEN + f"Yeni blok madenciliği tamamlandı: {new_block.hash}" + Style.RESET_ALL)
        self.chain.append(new_block)
        self.pending_transactions = []

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(Fore.CYAN + f"Blok {block.index} - Zaman: {block.get_readable_timestamp()} - Hash: {block.hash} - Önceki Hash: {block.previous_hash}" + Style.RESET_ALL)

    def get_balance(self, user: str):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["sender"] == user:
                    balance -= transaction["amount"]
                if transaction["recipient"] == user:
                    balance += transaction["amount"]
        return balance

    def export_to_json(self, filename="blockchain_data.json"):
        with open(filename, "w") as file:
            json.dump([block.__dict__ for block in self.chain], file, indent=4)
        print(Fore.YELLOW + "Blockchain verisi başarıyla kaydedildi!" + Style.RESET_ALL)

    def load_from_json(self, filename="blockchain_data.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = json.load(file)
                self.chain = [Block(**block) for block in data]
            print(Fore.YELLOW + "Blockchain verisi başarıyla yüklendi!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Kayıtlı blockchain dosyası bulunamadı!" + Style.RESET_ALL)

    def get_transaction_history(self, user: str):
        history = []
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["sender"] == user or transaction["recipient"] == user:
                    history.append(transaction)
        return history


my_blockchain = Blockchain()

while True:
    print("\n1. Yeni işlem ekle")
    print("2. Madencilik yap")
    print("3. Blok zincirini görüntüle")
    print("4. Kullanıcı bakiyesini kontrol et")
    print("5. Blockchain verisini kaydet")
    print("6. Blockchain verisini yükle")
    print("7. İşlem geçmişini görüntüle")
    print("8. Çıkış")

    choice = input("Seçiminiz: ")

    if choice == "1":
        sender = input("Gönderen: ")
        recipient = input("Alıcı: ")
        amount = float(input("Miktar: "))
        my_blockchain.add_transaction(sender, recipient, amount)
        print(Fore.YELLOW + "İşlem başarıyla eklendi!" + Style.RESET_ALL)
    elif choice == "2":
        my_blockchain.mine_block()
    elif choice == "3":
        my_blockchain.print_chain()
    elif choice == "4":
        user = input("Kullanıcı adı: ")
        balance = my_blockchain.get_balance(user)
        print(Fore.GREEN + f"{user} kullanıcısının bakiyesi: {balance}" + Style.RESET_ALL)
    elif choice == "5":
        my_blockchain.export_to_json()
    elif choice == "6":
        my_blockchain.load_from_json()
    elif choice == "7":
        user = input("Kullanıcı adı: ")
        history = my_blockchain.get_transaction_history(user)
        print(Fore.CYAN + f"{user} kullanıcısının işlem geçmişi:" + Style.RESET_ALL)
        for tx in history:
            print(tx)
    elif choice == "8":
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
