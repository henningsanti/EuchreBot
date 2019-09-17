CARD_CONFIG = {
    'x': 100,
    'y': 150,
    'padx': 20
}

BTN_CONFIG = {
    'width': 20,
    'height': 1,
}


SUITS = {'h' : 'Hearts',
         'd' : 'Diamonds',
         'c' : 'Clubs',
         's' : 'Spades'
}

SLEEPTIME = 0

INFO_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 10)
CARD_FONT = ("Helvetica", 16)
BIG_FONT = ("Helvetica", 20)
HUGE_FONT = ("Helvetica", 32)

def is_lefty(card, trump):
    if card.value == 'J':
        if trump == 'd':
            return card.suit == 'h'

        elif trump == 'h':
            return card.suit == 'd'

        elif trump == 's':
            return card.suit == 'c'

        else:
            return card.suit == 's'

    else:
        return False

def validate_play_card(lead_card, card, trump, hand):
    if lead_card == None:
        return True

    lead_suit = lead_card.suit if not is_lefty(lead_card, trump) else trump
    card_suit = card.suit if not is_lefty(card, trump) else trump

    if card_suit == lead_suit:
        return True

    else:
        for c in hand:
            c_suit = c.suit if not is_lefty(c, trump) else trump
            if not c == card and len(hand) > 1:
                if c_suit == lead_suit:
                    return False
        return True

#----------------------------------------------------------------
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

    if lead_suit == None:
        return base_compare(card1, card2, hierarchy)

    if not card1.suit == lead_suit:
        return 1

    elif not card2.suit == lead_suit:
        return -1

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