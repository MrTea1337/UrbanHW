from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy_count = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while enemy_count > 0:
            enemy_count -= self.power
            sleep(1)
            day += 1
            print(f"{self.name} сражается {day} день(дня)..., осталось {enemy_count} воинов.")
            if enemy_count <= 0:
                print(f"{self.name} одержал победу спустя {day} дней(дня)!")


second_knight = Knight("Sir Galahad", 20)
first_knight = Knight('Sir Lancelot', 10)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')