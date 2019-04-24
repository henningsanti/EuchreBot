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

def validate_play_card(lead_suit, card, trump, hand):
    if lead_suit == None:
        return True

    if card.suit == lead_suit:
        return True

    elif is_lefty(card, trump) and lead_suit == trump:
        return True

    else:
        for icard in hand:
            if not icard == card and len(hand) > 1:
                if icard.suit == lead_suit:
                    return False
                elif is_lefty(icard, trump) and lead_suit == trump:
                    return False
        return True
