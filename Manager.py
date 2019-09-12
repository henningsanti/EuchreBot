from RandomDecider import RandomDecider

class Manager:
    def __init__(self):
        self.players = [RandomDecider(id=0,team=0, mgr=self, player=Player), RandomDecider(id=1,team=1, mgr=self), RandomDecider(id=2,team=0, mgr=self), RandomDecider(id=3,team=1, mgr=self)]
