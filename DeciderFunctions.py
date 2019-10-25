from Utilities import *
from DeciderUtilities import *
from Model import BidDecision, SecondBidDecision
from functools import cmp_to_key

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

def decide_second_bid_conservative(hand, top_card):
    my_suits = list(SUITS.keys())
    my_suits.remove(top_card.suit)

    bid_decisions = {}

    for suit in my_suits:
        bid_decisions[suit] = decide_bid_conservative(hand, suit)

    for suit, decision in bid_decisions.items():
        if decision.bid and decision.alone:
            return SecondBidDecision(selected=True, trump=suit, alone=True)

    for suit, decision in bid_decisions.items():
        if decision.bid:
            return SecondBidDecision(selected=True, trump=suit, alone=False)

    return SecondBidDecision(selected=False, trump=None, alone=False)

def play_card_simple(hand, trump, field, low):
    playable_cards = []
    lead_card = None if len(field) == 0 else field[0][1]
    lead_suit = None if lead_card == None else lead_card.suit

    for card in hand:
        if validate_play_card(lead_card=lead_card, card=card, trump=trump, hand=hand):
            playable_cards.append(card)

    sorted_cards = sorted(playable_cards, key=cmp_to_key(Sorter(lead_suit, trump).compare_cards), reverse=low)

    return sorted_cards[0]

def play_card_cautious(hand, trump, field, player_id):
    playable_cards = []
    field_cards = {}

    lead_card = None if len(field) == 0 else field[0][1]
    lead_suit = None if lead_card == None else lead_card.suit

    for id, card in field:
        field_cards[card] = id

    for card in hand:
        if validate_play_card(lead_card=lead_card, card=card, trump=trump, hand=hand):
            playable_cards.append(card)

    sorted_field = sorted(list(field_cards.keys()), key=cmp_to_key(Sorter(lead_suit, trump).compare_cards))
    sorted_cards = sorted(playable_cards, key=cmp_to_key(Sorter(lead_suit, trump).compare_cards))

    if not bool(field_cards):
        return sorted_cards[0]

    elif get_team_by_player_id(field_cards[sorted_field[0]]) == get_team_by_player_id(player_id):
        return sorted_cards[-1]

    elif Sorter(lead_suit, trump).compare_cards(sorted_cards[0], sorted_field[0]) == -1:
        return sorted_cards[0]

    else:
        return sorted_cards[-1]

def swap_card(hand, trump, top_card):
    sorted_cards = sorted(hand, key=cmp_to_key(Sorter(None, trump).compare_cards), reverse=True)
    return sorted_cards[0]
