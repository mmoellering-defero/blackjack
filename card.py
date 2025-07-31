class Card():
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_suit_symbol(self) -> str:
        match self.suit:
            case 'C':
                return '♣'
            case 'S':
                return '♠'
            case 'H':
                return '♥'
            case 'D':
                return '♦'

    def display(self, hidden: bool = False) -> str:
        extra_space = ' '

        rank = '?' if hidden else self.rank
        suit_symbol = '?' if hidden else self.get_suit_symbol()

        if len(rank) == 2:
            extra_space = ''

        return f'{rank} {extra_space}{suit_symbol}'
