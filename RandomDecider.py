from GUIPlayer import *
from Model import *
from Utilities import *
import time
import random

class RandomDecider():
    def setPlayer(self, player):
        self.player = player

    def bid(self, top_card):
        time.sleep(SLEEPTIME)

        bid = True if random.randint(0,1) == 0 else False
        alone = True if random.randint(0,1) == 0 else False

        return BidDecision(bid=bid, alone=alone)

    def second_bid(self, top_card):
        time.sleep(SLEEPTIME)

        my_suits = list(SUITS.keys())
        my_suits.remove(top_card.suit)
        choice = random.randint(0,2)
        trump = my_suits[choice]
        selected = True if random.randint(0,1) == 0 else False
        alone = True if random.randint(0,1) == 0 else False

        return SecondBidDecision(selected=selected, trump=trump, alone=alone)

    def play_card(self, field):
        time.sleep(SLEEPTIME)

        my_list = []
        lead_card = None if len(field) == 0 else field[0][1]

        for card in self.player.hand:
            if validate_play_card(lead_card=lead_card, card=card, trump=self.player.game_state.trump, hand=self.player.hand):
                my_list.append(card)

        choice = random.randint(0,len(my_list)-1)
        return my_list[choice]

    def swap_card(self, top_card):
        time.sleep(SLEEPTIME)

        choice = random.randint(0,4)
        return self.player.hand[choice]
