from Graveyard import Graveyard

class GameState:
    def __init__(self, dealer_id, team_scores):
        self.dealer_id = dealer_id
        self.team_tricks = [0, 0]
        self.team_scores = team_scores
        self.trump = None
        self.alone = None
        self.making_team = None
        self.graveyard = Graveyard(dealer_id)

class BidDecision:
    def __init__(self, bid, alone):
        self.bid = bid
        self.alone = alone

class SecondBidDecision:
    def __init__(self, selected, trump, alone):
        self.selected = selected
        self.trump = trump
        self.alone = alone
