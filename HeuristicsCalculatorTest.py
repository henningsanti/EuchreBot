from DeciderUtilities import calculate_heuristics
from Utilities import *
from Euchre import Card
import unittest

class TestHeuristicsCalculator(unittest.TestCase):
    def test_no_lead_suit(self):
        trump = 'h'
        lead_suit = None

        expected = {
            Card('9', 'h'): 100,
            Card('T', 'h'): 200,
            Card('J', 'h'): 1500,
            Card('Q', 'h'): 400,
            Card('K', 'h'): 500,
            Card('A', 'h'): 600,
            Card('9', 'c'): 1,
            Card('T', 'c'): 2,
            Card('J', 'c'): 3,
            Card('Q', 'c'): 4,
            Card('K', 'c'): 5,
            Card('A', 'c'): 6,
            Card('9', 'd'): 1,
            Card('T', 'd'): 2,
            Card('J', 'd'): 1000,
            Card('Q', 'd'): 4,
            Card('K', 'd'): 5,
            Card('A', 'd'): 6,
            Card('9', 's'): 1,
            Card('T', 's'): 2,
            Card('J', 's'): 3,
            Card('Q', 's'): 4,
            Card('K', 's'): 5,
            Card('A', 's'): 6
        }

        result = calculate_heuristics(trump, lead_suit)

        for suit in c_suits:
            for value in c_values:
                card = Card(value, suit)
                self.assertEqual(result[card], expected[card])

    def test_lead_suit_does_not_equal_trump(self):
        trump = 'h'
        lead_suit = 'c'

        expected = {
            Card('9', 'h'): 100,
            Card('T', 'h'): 200,
            Card('J', 'h'): 1500,
            Card('Q', 'h'): 400,
            Card('K', 'h'): 500,
            Card('A', 'h'): 600,
            Card('9', 'c'): 10,
            Card('T', 'c'): 20,
            Card('J', 'c'): 30,
            Card('Q', 'c'): 40,
            Card('K', 'c'): 50,
            Card('A', 'c'): 60,
            Card('9', 'd'): 1,
            Card('T', 'd'): 2,
            Card('J', 'd'): 1000,
            Card('Q', 'd'): 4,
            Card('K', 'd'): 5,
            Card('A', 'd'): 6,
            Card('9', 's'): 1,
            Card('T', 's'): 2,
            Card('J', 's'): 3,
            Card('Q', 's'): 4,
            Card('K', 's'): 5,
            Card('A', 's'): 6
        }

        result = calculate_heuristics(trump, lead_suit)

        for suit in c_suits:
            for value in c_values:
                card = Card(value, suit)
                self.assertEqual(result[card], expected[card])

    def test_lead_suit_does_equal_trump(self):
        trump = 'h'
        lead_suit = 'h'

        expected = {
            Card('9', 'h'): 100,
            Card('T', 'h'): 200,
            Card('J', 'h'): 1500,
            Card('Q', 'h'): 400,
            Card('K', 'h'): 500,
            Card('A', 'h'): 600,
            Card('9', 'c'): 1,
            Card('T', 'c'): 2,
            Card('J', 'c'): 3,
            Card('Q', 'c'): 4,
            Card('K', 'c'): 5,
            Card('A', 'c'): 6,
            Card('9', 'd'): 1,
            Card('T', 'd'): 2,
            Card('J', 'd'): 1000,
            Card('Q', 'd'): 4,
            Card('K', 'd'): 5,
            Card('A', 'd'): 6,
            Card('9', 's'): 1,
            Card('T', 's'): 2,
            Card('J', 's'): 3,
            Card('Q', 's'): 4,
            Card('K', 's'): 5,
            Card('A', 's'): 6
        }

        result = calculate_heuristics(trump, lead_suit)

        for suit in c_suits:
            for value in c_values:
                card = Card(value, suit)
                self.assertEqual(result[card], expected[card])

if __name__ == '__main__':
    unittest.main()
