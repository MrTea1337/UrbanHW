import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.test_runner_1 = Runner("Усэйн", 10)
        self.test_runner_2 = Runner("Андрей", 9)
        self.test_runner_3 = Runner("Ник", 3)
        self.distance = 90

    def test_usain_and_nick(self):
        tournament = Tournament(self.distance, self.test_runner_3, self.test_runner_1, )
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(self.distance, self.test_runner_3, self.test_runner_2, )
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_all_runners(self):
        tournament = Tournament(self.distance, self.test_runner_3, self.test_runner_2, self.test_runner_1, )
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for test_num, result in reversed(cls.all_results.items()):
            print(result)


if __name__ == "__main__":
    unittest.main()
