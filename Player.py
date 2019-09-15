class Player():
    def __init__(self, id, team, decider):
        self.id = id
        self.team = team
        self.hand = []
        self.game_state = None
        self.decider = decider
        self.decider.setPlayer(self)

    def bid(self, top_card):
        return self.decider.bid(top_card)

    def second_bid(self, top_card):
        return self.decider.second_bid(top_card)

    def swap_card(self, top_card):
        return self.decider.swap_card(top_card)

    def play_card(self, field):
        return self.decider.play_card(field)
