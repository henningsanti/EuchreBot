from Model import *
class Player:
    def __init__(self, id, team):
        self.id = id
        self.team = team
        self.hand = []
        self.game_state = None

    def bid(self, top_card):
        return BidDecision(False, False)

    def second_bid(self, top_card):
        return SecondBidDecision(True, 'd', True)

    def swap_card(self):
        return self.hand[0]

    def play_card(self, field):
        return self.hand[0]