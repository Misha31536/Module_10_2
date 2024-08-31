import threading
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)


    def run(self):
        print(f'{self.name}, На нас напали')
        enemy = 100
        day = 0
        while enemy > 0:
            day += 1
            enemy = enemy - self.power
            sleep(1) # По прошествию 1 дня сражения (1 секунды) выводится строка
            # "<Имя рыцаря> сражается <кол-во дней>...,
            # осталось <кол-во воинов> воинов."
            print(f'{self.name} сражается {day} день(дней), осталось {enemy} войнов', end = '' + '\n' )
        # После победы над всеми врагами выводится надпись
        # "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
        print(f'{self.name} одержал победу спустя {day} дней(дня)')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()


