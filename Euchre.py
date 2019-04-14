import random

class Card:

    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit

class Dealer:

    def __init__(self):
        ''' Initialization...

            PARAMETERS:

                None

            RETURNS:

                Dealer object

            '''

        c_values = ['A',
                    'K',
                    'Q',
                    'J',
                    'T',
                    '9']
        c_suits = ['d',
                   'h',
                   'c',
                   's']

        self.deck = [Card(value=x, suit=y) for x in c_values for y in c_suits]
        random.shuffle(self.deck)

    def deal_card(self):
        cards = self.deck
        num_cards = len(cards)
        rand_card = random.randint(0, num_cards-1)

        if num_cards != 0:
            card = cards.pop(rand_card)
            return card

        else:
            print("No more cards in deck.")
            return None

    def deal(self, players):
        for player in players:
            player.hand = []
            for i in range(5):
                player.hand.append(self.deal_card())

    def shuffle_deck(self):
        random.shuffle(self)


class Player:

    def __init__(self, id=None, team=None):

        self.id = id
        self.team = team
        self.hand = []

class Round:

    def __init__(self, players):
        self.players = players
        self.dealer = Dealer()
        self.dealer.deal(players=self.players)

    def play_round(self):
        return [10,1]

class Match:

    def __init__(self):
        self.players = [Player(id=0,team=0), Player(id=1,team=1), Player(id=2,team=0), Player(id=3,team=1)]
        self.team_scores = [0,0]
        results = self.play_round()
        self.team_scores[0] += results[0]
        self.team_scores[1] += results[1]

    def play_round(self):
        round = Round(players=self.players)
        return round.play_round()
