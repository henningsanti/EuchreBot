from RandomDecider import RandomDecider
from HighConservativeDecider import HighConservativeDecider
from Player import Player
import logging

logging.basicConfig(filename='game.log', level=logging.INFO, format='%(message)s')

class Manager:
    def __init__(self):
        self.players = [
            Player(id=0, team= 0, decider=HighConservativeDecider()),
            Player(id=1, team= 1, decider=RandomDecider()),
            Player(id=2, team= 0, decider=RandomDecider()),
            Player(id=3, team= 1, decider=RandomDecider())
        ]

    def handle_trick_win(self, winner, field, index):
        pass
        # logging.info('Trick won: ' + str(winner.team))

    def handle_game_win(self, winners, team_scores):
        logging.info('' + str(winners))
