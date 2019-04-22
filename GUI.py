from Model import *
from tkinter import *
import sys
from GUIDecider import GUIDecider

class GUIManager():
    def __init__(self):
        self.root = Tk()
        self.root.geometry(("800x600"))
        self.root.title("Euchre")

        self.field_canvas = Canvas(self.root,width=600,height=400,bg="green")
        self.info_canvas = Canvas(self.root,width=200,height=400,bg="grey")
        self.hand_canvas = Canvas(self.root,width=600,height=200,bg="red")
        self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")

        self.field_canvas.grid(row=0, column=0)
        self.info_canvas.grid(row=0, column=1)
        self.hand_canvas.grid(row=1, column=0)
        self.action_canvas.grid(row=1, column=1)

        self.players = [GUIDecider(id=0,team=0, mgr=self), GUIDecider(id=1,team=1, mgr=self), GUIDecider(id=2,team=0, mgr=self), GUIDecider(id=3,team=1, mgr=self)]

    def render_game_win(self):
        self.refresh_canvases()
        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue
        return

    def refresh_canvases(self):
        self.hand_canvas.destroy()
        self.action_canvas.destroy()
        self.info_canvas.destroy()
        self.field_canvas.destroy()

        self.field_canvas = Canvas(self.root,width=600,height=400,bg="green")
        self.info_canvas = Canvas(self.root,width=200,height=400,bg="grey")
        self.hand_canvas = Canvas(self.root,width=600,height=200,bg="red")
        self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")

        self.field_canvas.grid(row=0, column=0)
        self.info_canvas.grid(row=0, column=1)
        self.hand_canvas.grid(row=1, column=0)
        self.action_canvas.grid(row=1, column=1)
