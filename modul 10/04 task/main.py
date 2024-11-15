import random
import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None     # Гость за столом, по умолчанию None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name    # Имя гостя

    def run(self):
        # Выбираем случайное время от 3 до 10 секунд, которое гость проведет за столом
        time_to_eat = random.randint(3, 10)
        time.sleep(time_to_eat)  # Гость "ест", поток засыпает на указанное время


class Cafe:
    def __init__(self, *tables):
        self.tables = tables  # Список столов в кафе
        self.queue = Queue()  # Очередь для ожидающих гостей

    def guest_arrival(self, *guests):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:  # Проверяем, свободен ли стол
                    table.guest = guest  # Сажаем гостя за стол
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    seated = True
                    break
            if not seated:  # Если не нашлось свободного стола
                self.queue.put(guest)  # Добавляем гостя в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        # Цикл работает, пока есть гости в очереди или за столами
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        new_guest = self.queue.get()
                        table.guest = new_guest
                        new_guest.start()
                        print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(1)  # Добавляем задержку для уменьшения нагрузки на процессор


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()