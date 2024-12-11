from threading import Lock, Thread
import time
import random
import threading


class Bank:


    def __init__(self):
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        transactions = 0
        while transactions <= 99:
            bk = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += bk
                print(f"Пополнение: {bk}. Балланс: {self.balance}\n")
            finally:
                self.lock.release()
            time.sleep(1)
            transactions += 1

    def take(self):
        transactions = 0
        while transactions <= 99:
            bk = random.randint(50, 500)
            print(f'Запрос на {bk}')
            self.lock.acquire()
            try:
                if bk <= self.balance:
                    self.balance -= bk
                    print(f'Снятие: {bk}. Балланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостатоно средств для списания {bk}')
            finally:
                self.lock.release()
            time.sleep(1)
            transactions += 1

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый балланс: {bk.balance}')