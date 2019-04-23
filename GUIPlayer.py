from tkinter import *
from Utilities import *

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
        self.hand_canvas.grid_remove()
        self.action_canvas.grid_remove()
        self.info_canvas.grid_remove()
        self.field_canvas.grid_remove()

        self.field_canvas = Canvas(self.root,width=600,height=400,bg="green")
        self.info_canvas = Canvas(self.root,width=200,height=400,bg="grey")
        self.hand_canvas = Canvas(self.root,width=600,height=200,bg="red")
        self.action_canvas = Canvas(self.root,width=200,height=200,bg="blue")

        self.field_canvas.grid(row=0, column=0)
        self.info_canvas.grid(row=0, column=1)
        self.hand_canvas.grid(row=1, column=0)
        self.action_canvas.grid(row=1, column=1)

    def render_hand(self):
        widgets = []
        widgets = self.root.winfo_children()
        for w in widgets:
            if w.winfo_children():
                widgets.extend(w.winfo_children())

        j = 0
        for widget in widgets:
            print('Widget {0}: '.format(j), widget)
            j += 1

        self.field_ids = {}

        for i in range(len(self.hand)):
            if i == 0:
                x = (604 - len(self.hand)*card_dims['x'] - (len(self.hand) - 1)*card_dims['padx'])/2

            else:
                x += card_dims['x'] + card_dims['padx']

            card_coords = (x, 25, x+card_dims['x'], 25+card_dims['y'])
            txt_coords = (x + 50, 100)

            my_id = self.hand_canvas.create_rectangle(card_coords, fill="white", tag='card-in-hand')
            my_id2 = self.hand_canvas.create_text(txt_coords, text=self.hand[i].__str__(), font=CARD_FONT, tag='card-in-hand')

            self.field_ids[str(my_id)] = self.hand[i]
            self.field_ids[str(my_id2)] = self.hand[i]


    def render_info(self):
        self.info_canvas.create_window((20, 30), anchor=W, window=Label(self.info_canvas, text='Player: '  + str(self.id), bg='grey', font=INFO_FONT))
        self.info_canvas.create_window((20, 70), anchor=W, window=Label(self.info_canvas, text='Dealer: '  + str(self.game_state.dealer_id), bg='grey', font=INFO_FONT))
        self.info_canvas.create_window((20, 110), anchor=W, window=Label(self.info_canvas, text='Team: '  + str(self.team), bg='grey', font=INFO_FONT))
        self.info_canvas.create_window((20, 150), anchor=W, window=Label(self.info_canvas, text='Trick Scores: '  + self.game_state.team_tricks.__str__(), bg='grey', font=INFO_FONT))
        self.info_canvas.create_window((20, 190), anchor=W, window=Label(self.info_canvas, text='Team Scores: '  + self.game_state.team_scores.__str__(), bg='grey', font=INFO_FONT))

    def bid(self, top_card):
        self.refresh_canvases()
        self.render_hand()
        self.render_info()

        card_coords = ((604 - card_dims['x'])/2, 125, (604 - card_dims['x'])/2 + card_dims['x'], 125+card_dims['y'])
        txt_coords = ((604 - card_dims['x'])/2 + card_dims['x']/2, 200)

        self.top_card = self.field_canvas.create_rectangle(card_coords, fill = "white")
        self.top_card_txt = self.field_canvas.create_text(txt_coords, text=top_card.__str__(), font=CARD_FONT)
        self.root.update()

    def second_bid(self, top_card):
        self.refresh_canvases()
        self.render_hand()
        self.render_info()

        txt_coords = ((604 - card_dims['x'])/2 + card_dims['x']/2, 200)
        self.field_canvas.create_text(txt_coords, text='Pick a Trump Suit', font=BIG_FONT)
        self.root.update()

    def swap_card(self):
        self.refresh_canvases()
        self.render_hand()
        self.render_info()

        self.root.update()

    def play_card(self, field):
        self.refresh_canvases()
        self.render_hand()
        self.render_info()

        for i in range(len(field)):
            if i == 0:
                x = (604 - len(field)*card_dims['x'] - (len(field) - 1)*card_dims['padx'])/2

            else:
                x += card_dims['x'] + card_dims['padx']

            card_coords = (x, 125, x+card_dims['x'], 125+card_dims['y'])
            txt_coords = (x + 50, 200)

            self.field_canvas.create_rectangle(card_coords, fill = "white")
            self.field_canvas.create_text(txt_coords, text=field[i].__str__(), font=CARD_FONT)

        self.root.update()
