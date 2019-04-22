from Model import *
from tkinter import *

card_dims = {
    'x': 100,
    'y': 150,
    'padx': 20
}
 
class GUIPlayer():
    def __init__(self, id, team, mgr):
        self.id = id
        self.team = team
        self.hand = []
        self.game_state = None

        self.field_canvas = mgr.field_canvas
        self.hand_canvas = mgr.hand_canvas
        self.action_canvas = mgr.action_canvas
        self.info_canvas = mgr.info_canvas
        self.root = mgr.root

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

    def render_hand(self):
        for i in range(len(self.hand)):
            if i == 0:
                x = (604 - len(self.hand)*card_dims['x'] - (len(self.hand) - 1)*card_dims['padx'])/2

            else:
                x += card_dims['x'] + card_dims['padx']

            card_coords = (x, 25, x+card_dims['x'], 25+card_dims['y'])
            txt_coords = (x + 50, 100)

            self.hand_canvas.create_rectangle(card_coords,
                                              fill = "white",
                                              tag="card_on_field")
            self.hand_canvas.create_text(txt_coords, text=self.hand[i].__str__())
        return

    def render_info(self):
        self.info_canvas.create_window((20, 20), anchor=W, window= Label(self.info_canvas, text='Player: '  + str(self.id), bg='grey'))
        self.info_canvas.create_window((20, 60), anchor=W, window= Label(self.info_canvas, text='Team: '  + str(self.team), bg='grey'))
        self.info_canvas.create_window((20, 100), anchor=W, window= Label(self.info_canvas, text='Trick Scores: '  + self.game_state.team_tricks.__str__(), bg='grey'))
        self.info_canvas.create_window((20, 140), anchor=W, window= Label(self.info_canvas, text='Team Scores: '  + self.game_state.team_scores.__str__(), bg='grey'))
        return

    def render_second_bid(self):
        return

    def render_trick(self):
        for i in range(4):
            if i == 0:
                x = 72

            else:
                x += card_dims['x'] + card_dims['padx']

            card_coords = (x, 125, x+card_dims['x'], 125+card_dims['y'])

            self.field_canvas.create_rectangle(card_coords,
                                               fill = "white",
                                               tag="card_on_field")
        
    def bid(self, top_card):
        self.refresh_canvases()
        self.render_hand()
        self.render_info()

        card_coords = ((604 - card_dims['x'])/2, 125, (604 - card_dims['x'])/2 + card_dims['x'], 125+card_dims['y'])
        txt_coords = ((604 - card_dims['x'])/2 + card_dims['x']/2, 200)

        self.top_card = self.field_canvas.create_rectangle(card_coords, fill = "white", tag="top_card")
        self.top_card_txt = self.field_canvas.create_text(txt_coords, text=top_card.__str__())

    def second_bid(self, top_card):
        pass

    def swap_card(self):
        pass

    def play_card(self, field):
        pass
