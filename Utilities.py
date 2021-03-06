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

c_values = ['A',
            'K',
            'Q',
            'J',
            'T',
            '9']
c_suits = ['d',
           'h',
           'c',
           's']

class Card:
    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        if other == None:
            return False
        return self.value == other.value and self.suit == other.suit

    def __str__(self):
        return self.value + ' ' + self.suit

    def __hash__(self):
        return hash((self.value, self.suit))

    __repr__ = __str__

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
