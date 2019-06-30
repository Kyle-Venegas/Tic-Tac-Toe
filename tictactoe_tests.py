#import tictactoe
import unittest
import tictactoe

class TestVictory(unittest.TestCase):
    def test_playerLetter(self):
        self.assertTrue('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
