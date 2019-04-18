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

        self.frameGame = Frame(self.root)
            #canvas for the game
        self.gameScreen = Canvas(self.frameGame,width=800,height=600,bg="green")
        self.frameGame.pack()
        self.gameScreen.pack()
        self.card = self.gameScreen.create_rectangle((400,250),(500,390),
                                                             fill = "blue",
                                                             tag="card_on_field",
                                                             outline="darkblue")
        self.root.mainloop()

    def bid(self, top_card):
        return BidDecision(bid=False, alone=False)

    def second_bid(self, top_card):
        return SecondBidDecision(selected=True, trump='d', alone=False)

    def swap_card(self):
        return self.hand[0]

    def play_card(self, field):
        return self.hand[0]