from Utilities import *

def get_team_by_player_id(player_id):
    if player_id == 1 or player_id == 3:
        return 1
    else:
        return 0

def calculate_heuristics(trump, lead_suit):
    base_scores = {'A': 6,
                   'K': 5,
                   'Q': 4,
                   'J': 3,
                   'T': 2,
                   '9': 1}

    result = {}

    for suit in c_suits:
        for value in c_values:
            multiplier = 1
            if suit == trump:
                multiplier = 100
            result[Card(value, suit)] = base_scores[value]*multiplier

    if not lead_suit == None and not lead_suit == trump:
        for value in c_values:
            result[Card(value, lead_suit)] *= 10

    # righty
    result[Card('J', trump)] = 1500
    # lefty
    for suit in c_suits:
        for value in c_values:
            card = Card(value, suit)
            if is_lefty(card, trump):
                result[card] = 1000
                break

    return result

# MARKOV RETARDED
# def calculate_points_left_over(played_cards, trump, lead_suit, field):
#     heuristics = calculate_heuristics(trump, lead_suit)
#
#     all_points = sum(heuristics.values())
#     used_points = sum([heuristics[card] for card in played_cards]) + \
#                   sum([heuristics[card[1]] for card in field])
#
#     return all_points - used_points
#
# def calculate_points_in_hand(trump, lead_suit, hand):
#     return sum([calculate_heuristics(trump, lead_suit)[card] for card in hand])

# TODO: implement me
def markov_decide(hand, trump, player_id, graveyard):
    pass

def base_compare(card1, card2, hierarchy):
    return -1 if hierarchy[card1.value] > hierarchy[card2.value] else 1

def compare_trumps(card1, card2):
    hierarchy = {'J': 5,
                'A': 4,
                'K': 3,
                'Q': 2,
                'T': 1,
                '9': 0}

    return base_compare(card1, card2, hierarchy)

def compare_non_trump(card1, card2, lead_suit):
    hierarchy = {'A': 5,
                'K': 4,
                'Q': 3,
                'J': 2,
                'T': 1,
                '9': 0}

    if not card1.suit == card2.suit:
        if card1.suit == lead_suit:
            return -1

        elif card2.suit == lead_suit:
            return 1

        else:
            return base_compare(card1, card2, hierarchy)

    else:
        return base_compare(card1, card2, hierarchy)

class Sorter:
    def __init__(self, lead_suit, trump):
        self.lead_suit = lead_suit
        self.trump = trump

    def compare_cards(self, card1, card2):
        if card1.suit == card2.suit:
            if card1.suit == self.trump:
                return compare_trumps(card1, card2)
            else:
                if is_lefty(card1, self.trump):
                    return -1
                elif is_lefty(card2,  self.trump):
                    return 1
                else:
                    return compare_non_trump(card1, card2, self.lead_suit)

        else:
            if card1.suit ==  self.trump and not is_lefty(card2,  self.trump):
                return -1

            elif card2.suit ==  self.trump and not is_lefty(card1,  self.trump):
                return 1

            elif card1.suit ==  self.trump and is_lefty(card2,  self.trump):
                if card1.value == 'J':
                    return -1
                else:
                    return 1

            elif card2.suit ==  self.trump and is_lefty(card1,  self.trump):
                if card2.value == 'J':
                    return 1
                else:
                    return -1

            else:
                if is_lefty(card1,  self.trump):
                    return -1
                elif is_lefty(card2,  self.trump):
                    return 1
                else:
                    return compare_non_trump(card1, card2, self.lead_suit)
