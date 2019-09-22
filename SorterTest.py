from Utilities import Sorter
from functools import cmp_to_key
from Euchre import Card
import unittest

class TestSorter(unittest.TestCase):
    def test_no_lead_suit(self):
        trump = 'h'
        hand =    [
            Card('K', 'h'),
            Card('A', 'd'),
            Card('J', 'd'),
            Card('Q', 'c'),
            Card('K', 'c')
        ]

        desired_hand =    [
            Card('J', 'd'),
            Card('K', 'h'),
            Card('A', 'd'),
            Card('K', 'c'),
            Card('Q', 'c')
        ]

        sorted_cards = sorted(hand, key=cmp_to_key(Sorter(None, trump).compare_cards))
        self.assertEqual(sorted_cards, desired_hand)

    def test_lead_suit(self):
        trump = 'h'
        lead_suit = 'c'
        hand =    [
            Card('K', 'h'),
            Card('K', 'd'),
            Card('J', 'd'),
            Card('Q', 'c'),
            Card('A', 'c')
        ]

        desired_hand =    [
            Card('J', 'd'),
            Card('K', 'h'),
            Card('A', 'c'),
            Card('Q', 'c'),
            Card('K', 'd')
        ]

        sorted_cards = sorted(hand, key=cmp_to_key(Sorter(lead_suit, trump).compare_cards))
        self.assertEqual(sorted_cards, desired_hand)

if __name__ == '__main__':
    unittest.main()
