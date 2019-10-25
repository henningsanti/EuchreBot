class Graveyard:
    def __init__(self, dealer_id):
        self.tricks = []
        self.dealer_id = dealer_id
        self.swapped_card = None

    def add_trick(self, trick):
        self.tricks.append(trick)

    def set_swapped_card(self, swapped_card):
        self.swapped_card = swapped_card
    
    def get_tricks(self):
        return self.tricks

    def get_all_cards(self, player_id):
        graveyard = [card[1] for trick in self.tricks for card in trick]

        if (player_id == self.dealer_id and not self.swapped_card == None):
            graveyard.append(self.swapped_card)
        
        return graveyard
