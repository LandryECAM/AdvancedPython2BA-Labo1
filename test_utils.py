# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEqual(utils.fact(4), 24)
        self.assertEqual(utils.fact(0), 1)
        with self.assertRaises(ValueError):
            utils.fact(-2)

    
    def test_roots(self):
        # À compléter...
        self.assertEqual(utils.roots(1, 0, -1), (1, -1))
    
    def test_integrate(self):
        # À compléter...
        self.assertEqual(utils.integrate('x', 0, 2), 2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
