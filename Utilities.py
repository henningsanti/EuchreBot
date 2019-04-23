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
         's' : 'Spades'}

SLEEPTIME = 0.5

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
