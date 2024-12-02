import threading
from time import sleep



class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.all_step = 100

    def run(self):
        day = 0
        print(f'{self.name}, на нас напали!')
        while self.all_step >0:
            self.all_step -= self.power
            sleep(1)
            day += 1
            print(f'{self.name} сражается {day}..., '
                  f'осталось {self.all_step} воинов')
        if self.all_step <= 0:
            print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились')