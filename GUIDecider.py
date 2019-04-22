from GUIPlayer import *
from Model import *

class GUIDecider(GUIPlayer):
    def __init__(self, id, team, mgr):
        super().__init__(id, team, mgr)
    
    def bid(self, top_card):
        super().bid(top_card)

        self.bid_button = Button(self.action_canvas, bg='white', text='BID', command=lambda: self.decide_bid(True, False))
        self.alone_button = Button(self.action_canvas, bg='white', text='GO ALONE', command=lambda: self.decide_bid(True, True))
        self.pass_button = Button(self.action_canvas, bg='white', text='PASS', command=lambda: self.decide_bid(False, False))

        self.bid_button.config(height=button_dims['height'], width=button_dims['width'],)
        self.alone_button.config(height=button_dims['height'], width=button_dims['width'])
        self.pass_button.config(height=button_dims['height'], width=button_dims['width'])

        self.action_canvas.create_window((100,40), window=self.bid_button)
        self.action_canvas.create_window((100,100), window=self.alone_button)
        self.action_canvas.create_window((100,160), window=self.pass_button)

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

        return BidDecision(bid=self.bid1, alone=self.alone)

    def decide_bid(self, bid, alone):
        self.bid1 = bid
        self.alone = alone
        self.selected = True

    def second_bid(self, top_card):
        return SecondBidDecision(selected=True, trump='d', alone=False)

    def swap_card(self):
        return self.hand[0]

    def play_card(self, field):
        return self.hand[0]
