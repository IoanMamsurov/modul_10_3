import threading
from random import randint
from time import sleep
lock = threading.Lock()



class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        counter = 0
        while counter < 100:
            a = randint(50, 500)
            self.balance += a
            counter += 1
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        counter = 0
        while counter < 100:
            a = randint(50, 500)
            print(f'Запрос на {a}')
            if a <= self.balance:
                self.balance -= a
                counter += 1
                print(f'Снятие: {a}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
