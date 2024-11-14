import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        while self.enemies > 0:
            day += 1
            self.enemies -= self.power
            days = 'дней'
            if day == 1:
                days = 'день'
            if day in [2, 3, 4]:
                days = 'дня'
            print(f'{self.name} сражается {day} {days}, осталось {self.enemies} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} {days}')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()