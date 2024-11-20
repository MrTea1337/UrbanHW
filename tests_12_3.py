import unittest
import runner
from runner_and_tournament import Runner, Tournament

is_frozen = False


class RunnerTest(unittest.TestCase):
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        walk_test_runner = runner.Runner('Danil')
        for _ in range(10):
            walk_test_runner.walk()
        self.assertEqual(walk_test_runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        run_test_runner = runner.Runner('Danil')
        for _ in range(10):
            run_test_runner.run()
        self.assertEqual(run_test_runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        challenge_test_runner_1 = runner.Runner('Biba')
        challenge_test_runner_2 = runner.Runner('Boba')
        for _ in range(10):
            challenge_test_runner_1.run()
            challenge_test_runner_2.walk()
        self.assertNotEqual(challenge_test_runner_1.distance, challenge_test_runner_2.distance)


is_frozen = True


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.test_runner_1 = Runner("Усэйн", 10)
        self.test_runner_2 = Runner("Андрей", 9)
        self.test_runner_3 = Runner("Ник", 3)
        self.distance = 90

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_usain_and_nick(self):
        tournament = Tournament(self.distance, self.test_runner_3, self.test_runner_1, )
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_andrey_and_nick(self):
        tournament = Tournament(self.distance, self.test_runner_3, self.test_runner_2, )
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
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
