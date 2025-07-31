from card import Card

class Person():
    def __init__(self, is_dealer: bool = False) -> None:
        self.chips = 1000000 if is_dealer else 1000
        self.cards: list[Card] = []

    def clear_hand(self):
        self.cards = []
