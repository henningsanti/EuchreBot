import random
from Player import Player
from Model import *

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

class Round:
    def __init__(self, players, dealer_id):
        self.players = players
        self.dealer = Dealer()
        self.dealer.deal(players=self.players)
        self.state = GameState(dealer_id)
        self.setGameStates()

    def start(self):
        if not self.bidding():
            return [0, 0]
        # bidding passed, no misdeal, game begins here
        self.play_tricks()
        return self.evaluate_scores()

    def play_tricks(self):
        player_id = findLeftOfPlayer(self.state.dealer_id, self.state.alone)
        for i in range(5):
            player_id = self.play_trick(player_id=player_id)

    def play_trick(self, player_id):
        field = []
        length = 4 if self.state.alone == None else 3

        for i in range(length):
            card_chosen = self.players[player_id].play_card(field)
            field.append((player_id, card_chosen))
            self.players[player_id].hand.remove(card_chosen)
            player_id = findLeftOfPlayer(player_id, self.state.alone)
        # decide who won
        winning_card = field[0]
        for card in field:
            winning_card = self.compare_cards(a=winning_card, b=card, lead_suit=field[0][1].suit)

        self.state.team_tricks[self.players[winning_card[0]].team] += 1

        # Testing for trick mechanics
        print('Trump: ' + self.state.trump)
        print(field)
        print('Winning Card: ' + winning_card[1].__str__())
        print('Winning Player: ', winning_card[0])
        print('Winning Team: ', self.players[winning_card[0]].team)
        print(self.state.team_tricks)
        print('Alone:', self.state.alone)
        print('Making team:', self.state.making_team)

        return winning_card[0]

    def bidding(self):
        top_card = self.dealer.deal_card()
        bidder = findLeftOfPlayer(self.state.dealer_id)
        for i in range(4):
            bid_result = self.players[bidder].bid(top_card)
            if not bid_result.bid:
                bidder =  findLeftOfPlayer(bidder)
            else:
                self.state.making_team = self.players[bidder].team
                if bid_result.alone:
                    self.state.alone = findLeftOfPlayer(findLeftOfPlayer(bidder))
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
                if bid_results.alone:
                    self.state.alone = findLeftOfPlayer(findLeftOfPlayer(bidder))
                self.state.making_team = self.players[bidder].team
                self.state.trump = bid_results.trump
                return True

        return False
    #TODO: Implement
    def evaluate_scores(self):
        return [2,1]

    def setGameStates(self):
        for player in self.players:
            player.game_state = self.state

    def compare_cards(self, a, b, lead_suit):
        card1 = a[1]
        card2 = b[1]

        if card1.suit == card2.suit:
            if card1.suit == self.state.trump:
                return self.compare_trumps(a, b)

            else:
                if self.is_lefty(card1):
                    return a
                elif self.is_lefty(card2):
                    return b
                else:
                    return self.compare_non_trump(a, b, lead_suit)

        else:
            if card1.suit == self.state.trump and not self.is_lefty(card2):
                return a

            elif card2.suit == self.state.trump and not self.is_lefty(card1):
                return b

            elif card1.suit == self.state.trump and self.is_lefty(card2):
                if card1.value == 'J':
                    return a
                else:
                    return b

            elif card2.suit == self.state.trump and self.is_lefty(card1):
                if card2.value == 'J':
                    return b
                else:
                    return a

            else:
                if self.is_lefty(card1):
                    return a
                elif self.is_lefty(card2):
                    return b
                else:
                    return self.compare_non_trump(a, b, lead_suit)

    def compare_trumps(self, a, b):
        card1 = a[1]
        card2 = b[1]

        hierarchy = {'J': 5,
                     'A': 4,
                     'K': 3,
                     'Q': 2,
                     'T': 1,
                     '9': 0}

        return a if hierarchy[card1.value] > hierarchy[card2.value] else b

    def compare_non_trump(self, a, b, lead_suit):
        card1 = a[1]
        card2 = b[1]

        if not card1.suit == lead_suit:
            return b

        elif not card2.suit == lead_suit:
            return a

        else:

            hierarchy = {'A': 5,
                         'K': 4,
                         'Q': 3,
                         'J': 2,
                         'T': 1,
                         '9': 0}

            return a if hierarchy[card1.value] > hierarchy[card2.value] else b

    def is_lefty(self, card):
        if card.value == 'J':
            if self.state.trump == 'd':
                return card.suit == 'h'

            elif self.state.trump == 'h':
                return card.suit == 'd'

            elif self.state.trump == 's':
                return card.suit == 'c'

            else:
                return card.suit == 's'

        else:
            return False


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

def findLeftOfPlayer(id, removed_id=None):
        if removed_id == None:
            if id == 3:
                return 0
            else:
                return id + 1
        else:
            if removed_id == findLeftOfPlayer(id):
                return findLeftOfPlayer(removed_id)
            else:
                return findLeftOfPlayer(id)
