from Utilities import is_lefty
from Model import BidDecision

def decide_bid_moderate(hand, suit):
    bid = False
    alone = False
    count = 0
    for card in hand:
        if is_lefty(card, suit):
            count += 1
        elif card.suit == suit:
            if card.value == 'A':
                count += 1
            elif card.value == 'J':
                count += 1
    if count >= 2:
        bid = True
        if count == 3:
            alone = True

    return BidDecision(bid, alone)

def decide_bid_conservative(hand, suit):
    bid = False
    alone = False
    count = 0
    foundAce = False

    for card in hand:
        if is_lefty(card, suit):
            count += 1
        elif card.suit == suit:
            if card.value == 'A':
                foundAce = True
            elif card.value == 'J':
                count += 1
    if count == 2:
        bid = True
        alone = foundAce

    return BidDecision(bid, alone)
