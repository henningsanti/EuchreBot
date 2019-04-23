from GUIPlayer import *
from Model import *
import time

class AIDecider(GUIPlayer):
    def __init__(self, id, team, mgr):
        super().__init__(id, team, mgr)

    def bid(self, top_card):
        super().bid(top_card)

        time.sleep(2)

        return BidDecision(bid=True, alone=False)

    def second_bid(self, top_card):
        super().second_bid(top_card)

        time.sleep(2)

        if top_card == 'd':
            trump = 'c'
        else:
            trump = 'd'

        return SecondBidDecision(selected=True, trump=trump, alone=self.alone)

    def play_card(self, field):
        super().play_card(field)

        time.sleep(2)

        return self.hand[0]
    
    def swap_card(self):
        super().swap_card()

        time.sleep(2)

        return self.hand[0]