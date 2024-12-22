import unittest
import logging

from modul_12.task_03 import main

# Настройка логирования
logging.basicConfig(filename='runner_tests.log', level=logging.INFO, filemode='w', encoding='UTF-8',
                    format='%(levelname)s: %(message)s')

def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        try:
            # Попытка создать объект Runner с отрицательной скоростью
            self.runner = main.Runner(name="Test Runner", speed=-5)
            self.runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: " + str(e))

    @skip_if_frozen
    def test_run(self):
        try:
            # Попытка создать объект Runner с некорректным типом для name
            self.runner = main.Runner(name=12345, speed=10)
            self.runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: " + str(e))