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

class Player:
    def __init__(self, id, team, game_state):
        self.id = id
        self.team = team
        self.hand = []
        self.game_state = game_state

    def bid():
        return BidDecision(False)

    def second_bid():
        return SecondBidDecision(False)

    def swap_card(card):
        return Card()

class GameState:
    def __init__(self):
        self.dealer_id = 0
        self.team_tricks = [0, 0]
        self.top_card = None
        self.trump = None

class SecondBidDecision:
    def __init__(self, selected, trump=None):
        self.selected = selected
        self.trump= trump

class BidDecision:
    def __init__(self, selected, card=None):
        self.selected = selected
        self.card = card

class Round:
    def __init__(self, players):
        self.players = players
        self.dealer = Dealer()
        self.dealer.deal(players=self.players)
        self.state = GameState()

    def play_round(self):
        if not self.bidding():
            self.state.dealer_id = findLeftOfPlayer(self.state.dealer_id)
            return [0, 0]
        
        self.state.dealer_id = findLeftOfPlayer(self.state.dealer_id)
        return self.evaluate_scores()

    def bidding(self):
        # dealer turns over top card
        # starting from dealer, each player has opportunity to select
        self.state.top_card = dealer.deal_card()
        for i in range(4):
            bidder = findLeftOfPlayer(self.state.dealer_id)
            bid_results = self.players[bidder].bid()
            if not bid_results.selected:
                bidder =  findLeftOfPlayer(bidder)
            else:
                self.state.trump= bid_results.card.suit
                dealer_decision = self.players[self.state.dealer_id].swap_card(bid_results.card)

                return True
        
        for i in range(4):
            bidder = findLeftOfPlayer(self.state.dealer_id)
            bid_results = self.players[bidder].second_bid(self.state)
            if not bid_results[0]:
                bidder =  findLeftOfPlayer(bidder)
            else:
                self.state.trump=bid_results[1]
                return True
        
        return False

    def evaluate_scores(self):
        return [10,1]

    

class Match:
    def __init__(self):
        self.players = [Player(id=0,team=0), Player(id=1,team=1), Player(id=2,team=0), Player(id=3,team=1)]
        self.team_scores = [0,0]
        
    def start_match(self):
        while True:
            results = self.play_round()
            self.team_scores[0] += results[0]
            self.team_scores[1] += results[1]
            if(check_end):
                return

    def play_round(self):
        round = Round(players=self.players)
        return round.play_round()
    
    def check_end(self):
        if self.team_scores[0] >= 10:
            print('Team 0 won')
            return True
        elif self.team_scores[1] >= 10:
            print('Team 1 won')
            return True
        else:
            return False

def findLeftOfPlayer(id):
        if id == 3:
            return 0
        else:
            return id + 1