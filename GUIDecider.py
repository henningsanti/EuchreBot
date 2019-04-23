from GUIPlayer import *
from Model import *
from Utilities import *


class GUIDecider(GUIPlayer):
    def __init__(self, id, team, mgr):
        super().__init__(id, team, mgr)

    def bid(self, top_card):
        super().bid(top_card)

        self.bid_button = Button(self.action_canvas, bg='white', text='Bid', font=BUTTON_FONT, command=lambda: self.decide_bid(True))
        self.pass_button = Button(self.action_canvas, bg='grey', text='Pass', font=BUTTON_FONT, command=lambda: self.decide_bid(False))

        self.bid_button.config(height=button_dims['height'], width=button_dims['width'],)
        self.pass_button.config(height=button_dims['height'], width=button_dims['width'])

        self.action_canvas.create_window((100,80), window=self.bid_button)
        self.action_canvas.create_window((100,120), window=self.pass_button)

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

        return BidDecision(bid=self.bid1, alone=self.alone)

    def second_bid(self, top_card):
        super().second_bid(top_card)

        suits = {'h' : 'Hearts',
                 'd' : 'Diamonds',
                 'c' : 'Clubs',
                 's' : 'Spades'}
        options = {}

        for key, pair in suits.items():
            if not key == top_card.suit:
                options[key] = pair

        self.suit1_button = Button(self.action_canvas, bg='white', text=options[list(options.keys())[0]], font=BUTTON_FONT, command=lambda: self.decide_second_bid(True, list(options.keys())[0]))
        self.suit2_button = Button(self.action_canvas, bg='white', text=options[list(options.keys())[1]], font=BUTTON_FONT, command=lambda: self.decide_second_bid(True, list(options.keys())[1]))
        self.suit3_button = Button(self.action_canvas, bg='white', text=options[list(options.keys())[2]], font=BUTTON_FONT, command=lambda: self.decide_second_bid(True, list(options.keys())[2]))
        self.pass_button = Button(self.action_canvas, bg='grey', text='Pass', font=BUTTON_FONT, command=lambda: self.decide_second_bid(False, None))

        self.suit1_button.config(height=button_dims['height'], width=button_dims['width'],)
        self.suit2_button.config(height=button_dims['height'], width=button_dims['width'])
        self.suit3_button.config(height=button_dims['height'], width=button_dims['width'])
        self.pass_button.config(height=button_dims['height'], width=button_dims['width'])

        self.action_canvas.create_window((100,40), window=self.suit1_button)
        self.action_canvas.create_window((100,80), window=self.suit2_button)
        self.action_canvas.create_window((100,120), window=self.suit3_button)
        self.action_canvas.create_window((100,160), window=self.pass_button)

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

        return SecondBidDecision(selected=self.bid2, trump=self.trump, alone=self.alone)

    def decide_bid(self, bid):
        self.bid1 = bid

        if bid:
            self.action_canvas.grid_remove()
            self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")
            self.action_canvas.grid(row=1, column=1)

            self.alone_button = Button(self.action_canvas, bg='white', text='Go Alone', font=BUTTON_FONT, command=lambda: self.decide_alone(True))
            self.not_alone_button = Button(self.action_canvas, bg='white', text='Go w/ Team', font=BUTTON_FONT, command=lambda: self.decide_alone(False))

            self.alone_button.config(height=button_dims['height'], width=button_dims['width'])
            self.not_alone_button.config(height=button_dims['height'], width=button_dims['width'])

            self.action_canvas.create_window((100,80), window=self.alone_button)
            self.action_canvas.create_window((100,120), window=self.not_alone_button)

            self.selected = False
            while not self.selected:
                self.root.update_idletasks()
                self.root.update()
                continue
        else:
            self.decide_alone(False)

        self.selected = True

    def decide_second_bid(self, bid, trump):
        self.bid2 = bid
        self.trump = trump

        if bid:
            self.action_canvas.grid_remove()
            self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")
            self.action_canvas.grid(row=1, column=1)

            self.alone_button = Button(self.action_canvas, bg='white', text='Go Alone', font=BUTTON_FONT, command=lambda: self.decide_alone(True))
            self.not_alone_button = Button(self.action_canvas, bg='white', text='Go w/ Team', font=BUTTON_FONT, command=lambda: self.decide_alone(False))

            self.alone_button.config(height=button_dims['height'], width=button_dims['width'])
            self.not_alone_button.config(height=button_dims['height'], width=button_dims['width'])

            self.action_canvas.create_window((100,80), window=self.alone_button)
            self.action_canvas.create_window((100,120), window=self.not_alone_button)

            self.selected = False
            while not self.selected:
                self.root.update_idletasks()
                self.root.update()
                continue
        else:
            self.decide_alone(False)

        self.selected = True

    def decide_alone(self, alone):
        self.alone = alone
        self.selected = True

    def swap_card(self):
        super().swap_card()
        return self.hand[0]

    def play_card(self, field):
        super().play_card(field)

        self.lead_suit = None
        if len(field) > 0:
            self.lead_suit = field[0][1].suit

        self.bingbingbing = Button(self.action_canvas, bg='white', text='Bing!', font=BUTTON_FONT, command=lambda: self.bing())
        self.bingbingbing.config(height=button_dims['height'], width=button_dims['width'])
        self.action_canvas.create_window((100,80), window=self.bingbingbing)

        self.hand_canvas.tag_bind('card-in-hand', '<Button-1>', self.play_this_card)

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

        return self.card_to_play

    def play_this_card(self, event):
        card_id = event.widget.find_closest(event.x, event.y)[0]
        self.card_to_play = self.field_ids[str(card_id)]
        print(self.game_state.trump)

        if self.lead_suit == None:
            self.selected = True
            return

        if self.card_to_play.suit == self.lead_suit:
            self.selected = True

        else:
            for card in self.hand:
                if not card == self.card_to_play and len(self.hand) > 1:
                    if card.suit == self.lead_suit:
                        self.selected = False
                        break

                    elif is_lefty(card, self.game_state.trump) and self.lead_suit == self.game_state.trump:
                        self.selected = False
                        break

                    else:
                        self.selected = True
                else:
                    self.selected = True
    def bing(self):
        self.card_to_play = self.hand[0]
        self.selected = True
