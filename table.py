from constants import MAX_DECKS, MAX_PLAYERS
from helpers import clear_screen
from person import Person
from shoe import Shoe

class Table():
    def __init__(self) -> None:
        while True:
            num_decks = input(f'\nHow many decks do you want to play with (1 - {MAX_DECKS})? ')
            if num_decks.isnumeric() and 1 <= int(num_decks) <= MAX_DECKS:
                break;
            print(f'\nPlease enter a number between 1 and {MAX_DECKS}.')

        self.shoe = Shoe(int(num_decks))

        while True:
            num_players = input(f'\nHow many players (1 - {MAX_PLAYERS})? ')
            if num_players.isnumeric() and 1 <= int(num_players) <= MAX_PLAYERS:
                break;
            print(f'\nPlease enter a number between 1 and {MAX_PLAYERS}.')

        num_players = int(num_players)
        self.players: list[Person] = []

        for _ in range(0, num_players):
            self.players.append(Person())

        self.dealer = Person(True)

    def clear_all_hands(self):
        for player in self.players:
            player.clear_hand()

        self.dealer.clear_hand()

    def deal_single_card(self, person: Person) -> None:
        person.cards.append(self.shoe.cards.pop(0))

    def deal_initial_cards(self):
        for _ in range(0, 2):
            for player in self.players:
                self.deal_single_card(player)

            self.deal_single_card(self.dealer)

        self.display()

    def display(self):
        clear_screen()

        for player_index, player in enumerate(self.players):
            print(f'\nPlayer {player_index + 1}:')
            for card in player.cards:
                print(card.display())

        print('\nDealer:')
        print(self.dealer.cards[0].display())
        print(self.dealer.cards[1].display(True))

        print(f'\nCards left in shoe: {len(self.shoe.cards)}')
        print(f'\nCards left before shuffle: {self.shoe.cards_remaining_before_shuffle()}')

    def play(self):
        while True:
            self.play_hand()

            if self.shoe.cards_remaining_before_shuffle() <= 0:
                print('\nTime to shuffle!\n')
                break

            if input('\nShould we play another hand (Y/N)? ') == 'N':
                print('\nSee ya next time!\n')
                break

            self.clear_all_hands()

    def play_hand(self):
        self.deal_initial_cards()

        for player_index, player in enumerate(self.players):
            while True:
                hit_or_stand = input(f'\nPlayer {player_index + 1}, hit or stand (H/S)? ')
                if hit_or_stand in ['H', 'S']:
                    break
                print(f'\nPlease enter H or S.')
            print(f'\n{hit_or_stand}')
