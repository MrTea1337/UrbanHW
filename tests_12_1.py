import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk_test_runner = runner.Runner('Danil')
        for _ in range(10):
            walk_test_runner.walk()
        self.assertEqual(walk_test_runner.distance, 50)
    def test_run(self):
        run_test_runner = runner.Runner('Danil')
        for _ in range(10):
            run_test_runner.run()
        self.assertEqual(run_test_runner.distance, 100)
    def test_challenge(self):
        challenge_test_runner_1 = runner.Runner('Biba')
        challenge_test_runner_2 = runner.Runner('Boba')
        for _ in range(10):
            challenge_test_runner_1.run()
            challenge_test_runner_2.walk()
        self.assertNotEqual(challenge_test_runner_1.distance, challenge_test_runner_2.distance)

if __name__ == "__main__":
    unittest.main()