import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    def setUp(self):
        self.usain = Runner('Усэйн', speed=10)
        self.andrey = Runner('Андрей', speed=9)
        self.nick = Runner('Ник', speed=3)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results['Usain and Nick'] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == 'Ник')

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results['Andrey and Nick'] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == 'Ник')

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results['Usain, Andrey and Nick'] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == 'Ник')


if __name__ == '__main__':
    unittest.main()
