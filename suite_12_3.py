import unittest
import tests_12_3


test_runner_tournament = unittest.TestSuite()

test_runner_tournament.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_runner_tournament.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

TextTestRunner = unittest.TextTestRunner(verbosity=2)
TextTestRunner.run(test_runner_tournament)
