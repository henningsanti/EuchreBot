import Euchre
from Model import *
from Player import Player
from tkinter import *
import tkinter.messagebox
import sys
from enum import Enum

class State(Enum):
    BIDDING = 1
    SECOND_BIDDING = 2
    TRICK = 3
    GAME_WIN = 4

class GUIPlayer(Player):
    def __init__(self, id, team):
        super(GUIPlayer, self).__init__(id, team)
        self.root = Tk()
        self.root.geometry(("800x600"))
        self.root.title("Euchre")

        # Create Frame Layout
        self.top_frame = Frame(self.root, width=800, height=400)
        self.bot_frame = Frame(self.root, width=800, height=200)

        self.field_frame = Frame(self.top_frame, width=600, height=400)
        self.info_frame = Frame(self.top_frame, width=200, height=400)
        self.hand_frame = Frame(self.bot_frame, width=600, height=200)
        self.action_frame = Frame(self.bot_frame, width=200, height=200)

        # Add Canvases to Frames
        self.field_canvas = Canvas(self.field_frame,width=600,height=400,bg="green")
        self.info_canvas = Canvas(self.info_frame,width=200,height=400,bg="grey")
        self.hand_canvas = Canvas(self.hand_frame,width=600,height=200,bg="red")
        self.action_canvas = Frame(self.action_frame, width=200, height=200, bg="black")

        # Pack Frames & Canvases
        self.top_frame.pack(fill=BOTH, side=TOP, expand=True)
        self.bot_frame.pack(fill=BOTH, side=BOTTOM, expand=True)

        self.field_frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.info_frame.pack(fill=BOTH, side=RIGHT, expand=True)

        self.hand_frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.action_frame.pack(fill=BOTH, side=RIGHT, expand=True)

        self.field_canvas.pack(fill=BOTH, expand=True)
        self.info_canvas.pack(fill=BOTH, expand=True)
        self.hand_canvas.pack(fill=BOTH, expand=True)
        self.action_canvas.pack(fill=BOTH, expand=True)

        self.card_dims = {
            'x': 100,
            'y': 150,
            'padx': 20
        }

        # tk.update_idletasks()
        # tk.update()
        #self.root.mainloop()

    def pack_frames(self):
        self.top_frame.pack(fill=BOTH, side=TOP, expand=True)
        self.bot_frame.pack(fill=BOTH, side=BOTTOM, expand=True)

        self.field_frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.info_frame.pack(fill=BOTH, side=RIGHT, expand=True)

        self.hand_frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.action_frame.pack(fill=BOTH, side=RIGHT, expand=True)

        self.field_canvas.pack(fill=BOTH, expand=True)
        self.info_canvas.pack(fill=BOTH, expand=True)
        self.hand_canvas.pack(fill=BOTH, expand=True)
        self.action_canvas.pack(fill=BOTH, expand=True)

    def render_hand(self):
        for i in range(5):
            if i == 0:
                x = 110

            else:
                x += self.card_dims['x'] + self.card_dims['padx']

            card_coords = (x, 25, x+self.card_dims['x'], 25+self.card_dims['y'])

            self.hand_canvas.create_rectangle(card_coords,
                                              fill = "white",
                                              tag="card_on_field")
        return

    def render_info(self):
        self.hand_canvas.create_rectangle(card_coords,
                                          fill = "white",
                                          tag="card_on_field")
        return

    def render_field_state(self, state):
        if state == State.BIDDING:
            self.render_bidding()
        elif state == State.SECOND_BIDDING:
            self.render_second_bidding()
        elif state == State.TRICK:
            self.render_trick()
        else:
            self.render_game_win()

    def render_bidding(self):

        return

    def render_second_bidding(self):
        return

    def render_trick(self):
        for i in range(4):
            if i == 0:
                x = 72

            else:
                x += self.card_dims['x'] + self.card_dims['padx']

            card_coords = (x, 125, x+self.card_dims['x'], 125+self.card_dims['y'])

            self.field_canvas.create_rectangle(card_coords,
                                               fill = "white",
                                               tag="card_on_field")

    def render_game_win(self):

        return

    def bid(self, top_card):
        my_canvas = Canvas(self.field_frame,width=600,height=400,bg="green")
        self.swap_field_canvas(my_canvas)

        my_canvas = Canvas(self.action_frame,width=200,height=200,bg="black")
        self.swap_action_canvas(my_canvas)

        card_coords = ((604 - self.card_dims['x'])/2,
                        125,
                        (604 - self.card_dims['x'])/2 + self.card_dims['x'],
                        125+self.card_dims['y'])

        txt_coords = ((604 - self.card_dims['x'])/2 + self.card_dims['x']/2,
                      200)

        self.top_card = self.field_canvas.create_rectangle(card_coords,
                                           fill = "white",
                                           tag="top_card")

        self.top_card_txt = self.field_canvas.create_text(txt_coords,
                                                          text=top_card.__str__())

        self.bid_button = Button(self.action_canvas,
                                 bg='white',
                                 text='BID',
                                 command=lambda: self.decide_bid(True, False))

        self.alone_button = Button(self.action_canvas,
                                  bg='white',
                                  text='GO ALONE',
                                  command=lambda: self.decide_bid(True, True))

        self.pass_button = Button(self.action_canvas,
                                  bg='white',
                                  text='PASS',
                                  command=lambda: self.decide_bid(False, False))

        self.pass_button.pack(side=TOP, fill=BOTH, pady=10, padx=5)
        self.alone_button.pack(side=TOP, fill=BOTH, pady=10, padx=5)
        self.bid_button.pack(side=TOP, fill=BOTH, pady=10, padx=5)

        self.root.update()

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

        return BidDecision(bid=self.bid1, alone=self.alone)

    def second_bid(self, top_card):
        return SecondBidDecision(selected=True, trump='d', alone=False)

    def swap_card(self):
        return self.hand[0]

    def play_card(self, field):
        # canvas1.tag_bind(buttonBG, "<Button-1>", clicked) ## when the square is clicked runs function "clicked".
        # canvas1.tag_bind(buttonTXT, "<Button-1>", clicked) ## same, but for the text.
        return self.hand[0]

    def decide_bid(self, bid, alone):
        self.bid1 = bid
        self.alone = alone
        self.selected = True

    def swap_field_canvas(self, canvas):
        self.field_canvas.destroy()
        self.field_canvas = canvas
        self.pack_frames()

    def swap_hand_canvas(self, canvas):
        self.hand_canvas.destroy()
        self.hand_canvas = canvas
        self.pack_frames()

    def swap_action_canvas(self, canvas):
        self.action_canvas.destroy()
        self.action_canvas = canvas
        self.pack_frames()
