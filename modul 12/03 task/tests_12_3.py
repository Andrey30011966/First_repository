import unittest
import main


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            test_func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = main.Runner('Усэйн', speed=5)

    @skip_if_frozen
    def test_run(self):
        initial_distance = self.runner.distance
        self.runner.run()
        self.assertEqual(self.runner.distance, initial_distance + self.runner.speed * 2,
                         f'Ожидалось, что расстояние увеличится на {self.runner.speed * 2}, '
                         f'но получилось {self.runner.distance - initial_distance}')

    @skip_if_frozen
    def test_walk(self):
        initial_distance = self.runner.distance
        self.runner.walk()
        self.assertEqual(self.runner.distance, initial_distance + self.runner.speed,
                         f'Ожидалось, что расстояние увеличится на {self.runner.speed}, '
                         f'но получилось {self.runner.distance - initial_distance}')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    @skip_if_frozen
    def setUp(self):
        self.usain = main.Runner('Усэйн', speed=10)
        self.andrey = main.Runner('Андрей', speed=9)
        self.nick = main.Runner('Ник', speed=3)

    @skip_if_frozen
    def test_race_usain_nick(self):
        tournament = main.Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results['Usain and Nick'] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == 'Ник')

    @skip_if_frozen
    def test_race_andrey_nick(self):
        tournament = main.Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results['Andrey and Nick'] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == 'Ник')

    @skip_if_frozen
    def test_race_usain_andrey_nick(self):
        tournament = main.Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results['Usain, Andrey and Nick'] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == 'Ник')


if __name__ == '__main__':
    unittest.main()
