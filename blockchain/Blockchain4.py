"""
Blockchain koduna manuel işlem ekleme özelliği ekleyelim. Bunun için, kullanıcıdan terminal aracılığıyla işlem bilgilerini alabileceğimiz bir yöntem ekleyeceğiz. İşlemler manuel olarak eklendiğinde, kullanıcının istediği zaman madencilik yapabilmesini sağlayacağız.

Şu değişiklikleri yapacağız:

Manuel işlem ekleme fonksiyonu: Kullanıcıdan gönderen, alıcı ve miktar bilgilerini alarak yeni bir işlem oluşturacak.
Manuel madencilik başlatma seçeneği: Kullanıcı belirli bir komutla madenciliği manuel olarak başlatabilecek.
Güncellenmiş kodu aşağıda bulabilirsin:

Blockchain Manual Add

Bunun yerine sohbette cevap ver
Kod güncellendi! Artık terminal üzerinden:

Yeni işlem ekleyebilir (Manuel olarak gönderen, alıcı ve miktar bilgilerini girebilirsiniz).
Madencilik işlemini manuel olarak başlatabilirsiniz (İşlemler madencilik yapılana kadar bekleyecek).
Blok zincirini görüntüleyebilir ve tüm işlemleri inceleyebilirsiniz.

"""


import time
import json
import hashlib
from typing import List
from datetime import datetime
from colorama import Fore, Style


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
            print(
                Fore.CYAN + f"Blok {block.index} - Zaman: {block.get_readable_timestamp()} - Hash: {block.hash} - Önceki Hash: {block.previous_hash}" + Style.RESET_ALL)

    def get_balance(self, user: str):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["sender"] == user:
                    balance -= transaction["amount"]
                if transaction["recipient"] == user:
                    balance += transaction["amount"]
        return balance

    def export_to_json(self):
        return json.dumps([block.__dict__ for block in self.chain], indent=4)

    def add_transaction_manually(self):
        sender = input("Gönderen: ")
        recipient = input("Alıcı: ")
        amount = float(input("Miktar: "))
        self.add_transaction(sender, recipient, amount)
        print(Fore.YELLOW + "İşlem başarıyla eklendi!" + Style.RESET_ALL)

    def mine_manually(self):
        user_choice = input("Madencilik yapmak ister misiniz? (evet/hayır): ")
        if user_choice.lower() == "evet":
            self.mine_block()
        else:
            print("Madencilik işlemi iptal edildi.")


my_blockchain = Blockchain()

while True:
    print("\n1. Yeni işlem ekle")
    print("2. Madencilik yap")
    print("3. Blok zincirini görüntüle")
    print("4. Çıkış")

    choice = input("Seçiminiz: ")

    if choice == "1":
        my_blockchain.add_transaction_manually()
    elif choice == "2":
        my_blockchain.mine_manually()
    elif choice == "3":
        my_blockchain.print_chain()
    elif choice == "4":
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
