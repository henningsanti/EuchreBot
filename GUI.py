from Model import *
from tkinter import *
from GUIDecider import *
from Utilities import *
from AIDecider import AIDecider

class GUIManager():
    def __init__(self):
        self.root = Tk()
        self.root.geometry(("800x600"))
        self.root.title("Euchre")
        #self.root.resizable(False, False)

        self.field_canvas = Canvas(self.root,width=600,height=400,bg="green")
        self.info_canvas = Canvas(self.root,width=200,height=400,bg="grey")
        self.hand_canvas = Canvas(self.root,width=600,height=200,bg="red")
        self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")

        self.field_canvas.grid(row=0, column=0)
        self.info_canvas.grid(row=0, column=1)
        self.hand_canvas.grid(row=1, column=0)
        self.action_canvas.grid(row=1, column=1)

        self.players = [GUIDecider(id=0,team=0, mgr=self), GUIDecider(id=1,team=1, mgr=self), GUIDecider(id=2,team=0, mgr=self), GUIDecider(id=3,team=1, mgr=self)]

    def render_game_win(self, winners, team_scores):
        self.hand_canvas.grid_remove()
        self.action_canvas.grid_remove()
        self.info_canvas.grid_remove()
        self.field_canvas.grid_remove()

        self.end_canvas = Canvas(self.root,width=800,height=600,bg="green")
        self.end_canvas.grid(row=0, column=0)

        txt_coords = (400, 200)
        text = 'Team {0} won with a score of {1} to {2}!'.format(winners, team_scores[winners], team_scores[0 if winners == 1 else 1])
        self.end_canvas.create_text(txt_coords, text=text, font=HUGE_FONT)

        self.killyourself = Button(self.end_canvas, bg='white', text='Kill Yourself', font=BUTTON_FONT, command=lambda: self.root.destroy())
        self.killyourself.config(height=button_dims['height'], width=button_dims['width'])
        self.end_canvas.create_window((400,300), window=self.killyourself)

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

    def render_trick_win(self, winner, field, index):
        self.field_canvas.grid_remove()
        self.hand_canvas.grid_remove()
        self.action_canvas.grid_remove()
        self.info_canvas.grid_remove()

        self.field_canvas = Canvas(self.root,width=600,height=400,bg="green")
        self.info_canvas = Canvas(self.root,width=200,height=400,bg="grey")
        self.hand_canvas = Canvas(self.root,width=600,height=200,bg="red")
        self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")

        self.field_canvas.grid(row=0, column=0)
        self.info_canvas.grid(row=0, column=1)
        self.hand_canvas.grid(row=1, column=0)
        self.action_canvas.grid(row=1, column=1)

        for i in range(len(field)):
            if i == 0:
                x = (604 - len(field)*card_dims['x'] - (len(field) - 1)*card_dims['padx'])/2

            else:
                x += card_dims['x'] + card_dims['padx']

            card_coords = (x, 125, x+card_dims['x'], 125+card_dims['y'])
            txt_coords = (x + 50, 200)

            if i == index:
                fill = 'lightgreen'
            else:
                fill = 'white'

            self.field_canvas.create_rectangle(card_coords, fill=fill)
            self.field_canvas.create_text(txt_coords, text=field[i].__str__(), font=CARD_FONT)

        txt_coords = (302, 62)
        text = 'Player {0} won a trick for Team {1}!\nPlayer {0} will start the next hand.'.format(winner.id, winner.team)
        self.field_canvas.create_text(txt_coords, text=text, font=BIG_FONT)

        self.boom = Button(self.field_canvas, bg='white', text='Continue', font=BUTTON_FONT, command=lambda: self.select())
        self.boom.config(height=button_dims['height'], width=button_dims['width'])
        self.field_canvas.create_window((302, 338), window=self.boom)

        self.selected = False
        while not self.selected:
            self.root.update_idletasks()
            self.root.update()
            continue

    def select(self):
        self.selected = True
