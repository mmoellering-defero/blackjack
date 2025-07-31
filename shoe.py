import math
import random
from card import Card

class Shoe():
    def __init__(self, num_decks: int) -> None:
        self.shuffle_count = max(math.ceil(num_decks * 52 / 3), 40)

        self.cards = []

        for suit in ['C', 'S', 'H', 'D']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                for _ in range(0, num_decks):
                    self.cards.append(Card(rank, suit))

        random.shuffle(self.cards)

    def cards_remaining_before_shuffle(self) -> int:
        return len(self.cards) - self.shuffle_count
