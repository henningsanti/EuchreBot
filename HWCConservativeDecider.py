import time
from DeciderFunctions import *

class HWCConservativeDecider():
    def setPlayer(self, player):
        self.player = player

    def bid(self, top_card):
        time.sleep(SLEEPTIME)
        return decide_bid_conservative(self.player.hand, top_card.suit)

    def second_bid(self, top_card):
        time.sleep(SLEEPTIME)
        return decide_second_bid_conservative(self.player.hand, top_card)

    def play_card(self, field):
        time.sleep(SLEEPTIME)
        return play_card_cautious(self.player.hand, self.player.game_state.trump, field, self.player.id)

    def swap_card(self, top_card):
        time.sleep(SLEEPTIME)
        sorted_cards = sorted(self.player.hand, key=cmp_to_key(Sorter(None, self.player.game_state.trump).compare_cards), reverse=True)
        return sorted_cards[0]
