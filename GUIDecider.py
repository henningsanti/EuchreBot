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

        self.bid_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'],)
        self.pass_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])

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
        options = {}

        for key, pair in SUITS.items():
            if not key == top_card.suit:
                options[key] = pair

        self.suit1_button = Button(self.action_canvas, bg='white', text=options[list(options.keys())[0]], font=BUTTON_FONT, command=lambda: self.decide_second_bid(True, list(options.keys())[0]))
        self.suit2_button = Button(self.action_canvas, bg='white', text=options[list(options.keys())[1]], font=BUTTON_FONT, command=lambda: self.decide_second_bid(True, list(options.keys())[1]))
        self.suit3_button = Button(self.action_canvas, bg='white', text=options[list(options.keys())[2]], font=BUTTON_FONT, command=lambda: self.decide_second_bid(True, list(options.keys())[2]))
        self.pass_button = Button(self.action_canvas, bg='grey', text='Pass', font=BUTTON_FONT, command=lambda: self.decide_second_bid(False, None))

        self.suit1_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'],)
        self.suit2_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])
        self.suit3_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])
        self.pass_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])

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
            self.action_canvas.destroy()
            self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")
            self.action_canvas.grid(row=1, column=1)

            self.alone_button = Button(self.action_canvas, bg='white', text='Go Alone', font=BUTTON_FONT, command=lambda: self.decide_alone(True))
            self.not_alone_button = Button(self.action_canvas, bg='white', text='Go w/ Team', font=BUTTON_FONT, command=lambda: self.decide_alone(False))

            self.alone_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])
            self.not_alone_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])

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
            self.action_canvas.destroy()
            self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")
            self.action_canvas.grid(row=1, column=1)

            self.alone_button = Button(self.action_canvas, bg='white', text='Go Alone', font=BUTTON_FONT, command=lambda: self.decide_alone(True))
            self.not_alone_button = Button(self.action_canvas, bg='white', text='Go w/ Team', font=BUTTON_FONT, command=lambda: self.decide_alone(False))

            self.alone_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])
            self.not_alone_button.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])

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

    def swap_card(self, top_card):
        super().swap_card(top_card)

        self.hand_canvas.tag_bind('card-in-hand', '<Button-1>', self.swap_this_card)

        txt_coords = (302, 62)
        text = 'Player {0}, pick a card from your hand to discard.'.format(self.id)
        self.field_canvas.create_text(txt_coords, text=text, font=BIG_FONT)

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

        return self.card_to_swap

    def play_card(self, field):
        super().play_card(field)

        self.lead_card = None if len(field) == 0 else field[0][1]

        # # Bing button allows you to play a random card for testing purposes
        # self.bingbingbing = Button(self.action_canvas, bg='white', text='Bing!', font=BUTTON_FONT, command=lambda: self.bing())
        # self.bingbingbing.config(height=BTN_CONFIG['height'], width=BTN_CONFIG['width'])
        # self.action_canvas.create_window((100,80), window=self.bingbingbing)

        self.hand_canvas.tag_bind('card-in-hand', '<Button-1>', self.play_this_card)

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

        return self.card_to_play

    def play_this_card(self, event):
        card_id = event.widget.find_closest(event.x, event.y)[0]
        self.card_to_play = self.hand_ids[str(card_id)]
        self.selected = validate_play_card(lead_card=self.lead_card, card=self.card_to_play, trump=self.game_state.trump, hand=self.hand)

    def swap_this_card(self, event):
        card_id = event.widget.find_closest(event.x, event.y)[0]
        self.card_to_swap = self.hand_ids[str(card_id)]
        self.selected = True

    def bing(self):
        self.card_to_play = self.hand[0]
        self.selected = True
