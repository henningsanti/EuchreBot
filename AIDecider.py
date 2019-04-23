from GUIPlayer import *
from Model import *
from Utilities import *
import time

class AIDecider(GUIPlayer):
    def __init__(self, id, team, mgr):
        super().__init__(id, team, mgr)

    def bid(self, top_card):
        super().bid(top_card)

        time.sleep(SLEEPTIME)

        return BidDecision(bid=True, alone=False)

    def second_bid(self, top_card):
        super().second_bid(top_card)

        time.sleep(SLEEPTIME)

        if top_card.suit == 'd':
            trump = 'c'
        else:
            trump = 'd'

        return SecondBidDecision(selected=True, trump=trump, alone=False)

    def play_card(self, field):
        super().play_card(field)

        time.sleep(SLEEPTIME)

        return self.hand[0]

    def swap_card(self, top_card):
        super().swap_card(top_card)

        time.sleep(SLEEPTIME)

        return self.hand[0]
