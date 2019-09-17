from Model import *
from Utilities import *
import time
import random
from Model import *
from DeciderFunctions import *
from functools import cmp_to_key

class HighConservativeDecider():
    def setPlayer(self, player):
        self.player = player

    # Here we implement our most naive bid algorithm
    def bid(self, top_card):
        time.sleep(SLEEPTIME)
            
        return decide_bid_conservative(self.player.hand, top_card.suit)

    def second_bid(self, top_card):
        time.sleep(SLEEPTIME)

        my_suits = list(SUITS.keys())
        my_suits.remove(top_card.suit)

        bid_decisions = {}

        for suit in my_suits:
            bid_decisions[suit] = decide_bid_conservative(self.player.hand, suit)
    
        for suit, decision in bid_decisions.iteritems():
            if decision.bid and decision.alone:
                return SecondBidDecision(selected=True, trump=suit, alone=True)

        for suit, decision in bid_decisions.iteritems():
            if decision.bid:
                return SecondBidDecision(selected=True, trump=suit, alone=False)

        return SecondBidDecision(selected=False, trump=None, alone=False)

                

    def play_card(self, field):
        time.sleep(SLEEPTIME)

        my_list = []
        lead_card = None if len(field) == 0 else field[0][1]
        lead_suit = None if lead_card == None else lead_card.suit

        for card in self.player.hand:
            if validate_play_card(lead_card=lead_card, card=card, trump=self.player.game_state.trump, hand=self.player.hand):
                my_list.append(card)

        print('sorting:')
        print('trump: ', self.player.game_state.trump)
        print('lead suit: ', lead_suit)
        sorted_cards = sorted(my_list, key=cmp_to_key(Sorter(lead_suit, self.player.game_state.trump).compare_cards))
        print('sorted list: ', sorted_cards)
        print('--------------')
        return sorted_cards[0]

    def swap_card(self, top_card):
        time.sleep(SLEEPTIME)

        sorted_cards = sorted(self.player.hand, key=cmp_to_key(Sorter(None, self.player.game_state.trump).compare_cards), reverse=True)
        return sorted_cards[0]
