"""
Akıllı Sözleşme Desteği: Kullanıcıların basit akıllı sözleşmeler oluşturmasını ve çalıştırmasını sağlayan bir yapı.
Ödül Mekanizması: Madencilik yapanlara ödül verme sistemi.
Zaman Damgası İyileştirmesi: Daha okunaklı ve detaylı zaman bilgisi ekleme.
Gelişmiş İşlem Doğrulama: İşlemlerin belirli kurallara göre doğrulanmasını sağlayan bir mekanizma.
Daha Kullanıcı Dostu Arayüz: Terminal üzerinden değil, bir web arayüzü ile blockchain yönetimi.

Kodunuza aşağıdaki geliştirmeleri ekledim:
Madencilik Ödülü: Madencilik yapanlara ödül olarak belirlenen miktarda coin verilir.
Madenci Takibi: Her bloğa madenciyi kaydeden bir alan eklendi.
İşlem Zaman Damgası: Her işleme, okunaklı bir tarih damgası eklendi.
İşlem Doğrulama: Gönderen ve alıcının aynı olması engellendi.
Geliştirilmiş Menü: Kullanıcı dostu bir etkileşimli terminal menüsü oluşturuldu.
"""

import time
import json
import hashlib
from typing import List, Dict
from datetime import datetime
from colorama import Fore, Style
import os


class Block:
    def __init__(self, index: int, previous_hash: str, transactions: List[dict], nonce: int = 0, miner: str = None):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.nonce = nonce
        self.miner = miner
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "nonce": self.nonce,
            "miner": self.miner
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_readable_timestamp(self) -> str:
        return datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[dict] = []
        self.difficulty = 4
        self.mining_reward = 10  # Madencilik ödülü
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(index=0, previous_hash="0", transactions=[], nonce=0, miner="Genesis")
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, recipient: str, amount: float):
        if sender == recipient:
            print(Fore.RED + "Gönderen ve alıcı aynı olamaz!" + Style.RESET_ALL)
            return
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def mine_block(self, miner_address: str):
        if not self.pending_transactions:
            print(Fore.RED + "İşlem kuyruğu boş, madencilik yapılamaz!" + Style.RESET_ALL)
            return None

        last_block = self.chain[-1]
        reward_transaction = {"sender": "Blockchain", "recipient": miner_address, "amount": self.mining_reward}
        self.pending_transactions.append(reward_transaction)

        new_block = Block(index=len(self.chain), previous_hash=last_block.hash, transactions=self.pending_transactions, miner=miner_address)

        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        print(Fore.GREEN + f"Yeni blok madenciliği tamamlandı: {new_block.hash}" + Style.RESET_ALL)
        self.chain.append(new_block)
        self.pending_transactions = []

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def get_balance(self, user: str) -> float:
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["sender"] == user:
                    balance -= transaction["amount"]
                if transaction["recipient"] == user:
                    balance += transaction["amount"]
        return balance

    def get_transaction_history(self, user: str) -> List[Dict]:
        history = []
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["sender"] == user or transaction["recipient"] == user:
                    history.append(transaction)
        return history


blockchain = Blockchain()

while True:
    print("\n1. Yeni işlem ekle")
    print("2. Madencilik yap")
    print("3. Blok zincirini görüntüle")
    print("4. Kullanıcı bakiyesini kontrol et")
    print("5. İşlem geçmişini görüntüle")
    print("6. Çıkış")

    choice = input("Seçiminiz: ")

    if choice == "1":
        sender = input("Gönderen: ")
        recipient = input("Alıcı: ")
        amount = float(input("Miktar: "))
        blockchain.add_transaction(sender, recipient, amount)
        print(Fore.YELLOW + "İşlem başarıyla eklendi!" + Style.RESET_ALL)
    elif choice == "2":
        miner = input("Madencinin adı: ")
        blockchain.mine_block(miner)
    elif choice == "3":
        for block in blockchain.chain:
            print(Fore.CYAN + f"Blok {block.index} - Zaman: {block.get_readable_timestamp()} - Hash: {block.hash} - Önceki Hash: {block.previous_hash} - Madenci: {block.miner}" + Style.RESET_ALL)
    elif choice == "4":
        user = input("Kullanıcı adı: ")
        balance = blockchain.get_balance(user)
        print(Fore.GREEN + f"{user} kullanıcısının bakiyesi: {balance}" + Style.RESET_ALL)
    elif choice == "5":
        user = input("Kullanıcı adı: ")
        history = blockchain.get_transaction_history(user)
        print(Fore.CYAN + f"{user} kullanıcısının işlem geçmişi:" + Style.RESET_ALL)
        for tx in history:
            print(tx)
    elif choice == "6":
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
