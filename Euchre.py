import random

class Card:
    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.value + ' ' + self.suit

    __repr__ = __str__

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
    def __init__(self, id, team):
        self.id = id
        self.team = team
        self.hand = []
        self.game_state = None

    def bid(self, top_card):
        return False

    def second_bid(self, top_card):
        return SecondBidDecision(True, 'd')

    def swap_card(self):
        return self.hand[0]

    def play_card(self, field):
        return self.hand[0]

class GameState:
    def __init__(self, dealer_id):
        self.dealer_id = dealer_id
        self.team_tricks = [0, 0]
        self.trump = None

class SecondBidDecision:
    def __init__(self, selected, trump=None):
        self.selected = selected
        self.trump= trump

class Round:
    def __init__(self, players, dealer_id):
        self.players = players
        self.dealer = Dealer()
        self.dealer.deal(players=self.players)
        self.state = GameState(dealer_id)
        self.setGameStates()

    def start(self):
        print(self.state.dealer_id)
        if not self.bidding():
            self.state.dealer_id = findLeftOfPlayer(self.state.dealer_id)
            return [0, 0]
        # bidding passed, no misdeal, game begins here
        self.play_tricks()

        self.state.dealer_id = findLeftOfPlayer(self.state.dealer_id)
        return self.evaluate_scores()

    def play_tricks(self):
        player = findLeftOfPlayer(self.state.dealer_id)
        for i in range(5):
            self.play_trick(player=player)
            player = findLeftOfPlayer(player)
    
    def play_trick(self, player):
        field = []
        for i in range(4):
            card_chosen = self.players[player].play_card(field)
            field.append(card_chosen)
            self.players[player].hand.remove(card_chosen)
            player = findLeftOfPlayer(player)
        
        
        # decide who won
        # append 1 to the trick count of that team

    def bidding(self):
        top_card = self.dealer.deal_card()
        bidder = findLeftOfPlayer(self.state.dealer_id)
        for i in range(4):
            bid_result = self.players[bidder].bid(top_card)
            if not bid_result:
                bidder =  findLeftOfPlayer(bidder)
            else:
                self.state.trump = top_card.suit
                dealer_decision = self.players[self.state.dealer_id].swap_card()

                self.players[self.state.dealer_id].hand.remove(dealer_decision)
                self.players[self.state.dealer_id].hand.append(top_card)
                return True
    
        bidder = findLeftOfPlayer(self.state.dealer_id)
        for i in range(4):
            bid_results = self.players[bidder].second_bid(top_card)
            if not bid_results.selected:
                bidder = findLeftOfPlayer(bidder)
            else:
                self.state.trump = bid_results.trump
                return True
        
        return False
    #TODO: Figure out dependencies and implement
    def evaluate_scores(self):
        return [2,1]

    def setGameStates(self):
        for player in self.players:
            player.game_state = self.state

class Match:
    def __init__(self):
        self.players = [Player(id=0,team=0), Player(id=1,team=1), Player(id=2,team=0), Player(id=3,team=1)]
        self.team_scores = [0,0]
        self.dealer_id = 0

    def start_match(self):
        while True:
            results = self.play_round()
            self.team_scores[0] += results[0]
            self.team_scores[1] += results[1]

            if(self.check_end()):
                return

            self.dealer_id = findLeftOfPlayer(self.dealer_id)

    def play_round(self):
        round = Round(players=self.players, dealer_id=self.dealer_id)
        return round.start()
    
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