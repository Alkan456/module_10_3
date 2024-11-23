import threading
from threading import Lock
from random import randint
from time import sleep




class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()




    def deposit(self):
        for i in range(1, 101):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            transaction = randint(50, 500)
            self.balance += transaction
            print(f'Пополнение №: {i}')
            print(f'Пополнение: {transaction}. Баланс: {self.balance}')
            sleep(0.001 )

    def take(self):
        for j in range(1, 101):
            transaction = randint(50, 500)
            print(f'Запрос на {transaction}')
            if transaction <= self.balance:
                self.balance -= transaction
                print(f'Снятие №: {j}')
                print(f'Снятие: {transaction}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bank = Bank()

thread1 = threading.Thread(target=Bank.deposit, args =(bank,))
thread2 = threading.Thread(target = Bank.take, args = (bank,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Итоговый баланс: {bank.balance}')
