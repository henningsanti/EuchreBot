from Euchre import Card
from DeciderFunctions import play_card_cautious
import unittest

class TestPlayCardCautious(unittest.TestCase):
    def test_no_field_plays_best_card(self):

        expected = Card('K', 'h')

        hand =    [
            Card('A', 'd'),
            expected,
            Card('J', 'c'),
            Card('Q', 'c'),
            Card('K', 'c')
        ]

        trump = 'h'
        field = []
        player_id = 1

        result = play_card_cautious(hand, trump, field, player_id)

        self.assertEqual(result, expected)

    def test_with_field_no_teammate_can_win_plays_best_card(self):

        expected = Card('K', 'c')

        hand =    [
            Card('A', 'd'),
            expected,
            Card('T', 'c'),
            Card('Q', 'c'),
            Card('K', 'h')
        ]

        trump = 'h'
        field = [(0, Card('9', 'c'))]
        player_id = 1

        result = play_card_cautious(hand, trump, field, player_id)

        self.assertEqual(result, expected)

    def test_with_field_no_teammate_cant_win_plays_worst_card(self):
        expected = Card('J', 's')

        hand =    [
            Card('A', 'd'),
            expected,
            Card('K', 'd'),
            Card('Q', 's'),
            Card('K', 's')
        ]

        trump = 'h'
        field = [(0, Card('9', 'c'))]
        player_id = 1

        result = play_card_cautious(hand, trump, field, player_id)

        self.assertEqual(result, expected)

    def test_with_field_teammate_winning_plays_worst_card(self):

        expected = Card('A', 'd')

        hand =    [
            Card('J', 'd'),
            expected,
            Card('J', 'h'),
            Card('Q', 'h'),
            Card('K', 'h')
        ]

        trump = 'h'
        field = [
            (0, Card('T', 'c')),
            (1, Card('9', 'c'))
        ]
        player_id = 2

        result = play_card_cautious(hand, trump, field, player_id)

        self.assertEqual(result, expected)

    def test_with_field_teammate_losing_can_win_plays_best_card(self):

        expected = Card('J', 'h')

        hand =    [
            Card('J', 'd'),
            expected,
            Card('A', 'd'),
            Card('Q', 'h'),
            Card('K', 'h')
        ]

        trump = 'h'
        field = [
            (0, Card('9', 'c')),
            (1, Card('T', 'c'))
        ]
        player_id = 2

        result = play_card_cautious(hand, trump, field, player_id)

        self.assertEqual(result, expected)

    def test_with_field_teammate_losing_cant_win_plays_worst_card(self):

        expected = Card('J', 's')

        hand =    [
            Card('J', 'd'),
            expected,
            Card('A', 'h'),
            Card('Q', 'h'),
            Card('K', 'h')
        ]

        trump = 'h'
        field = [
            (0, Card('9', 'c')),
            (1, Card('J', 'h'))
        ]
        player_id = 2

        result = play_card_cautious(hand, trump, field, player_id)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
