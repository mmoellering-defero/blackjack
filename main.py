import random

def get_shoe_cards(num_decks: int = 1) -> list[dict]:
    shoe_cards = []
    for suit in ['C', 'S', 'H', 'D']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            for i in range(0, num_decks):
                shoe_cards.append({
                    'rank': rank,
                    'suit': suit,
                })

    random.shuffle(shoe_cards)

    return shoe_cards

def display_suit_symbol(suit: str) -> str:
    match suit:
        case 'C':
            return '♣'
        case 'S':
            return '♠'
        case 'H':
            return '♥'
        case 'D':
            return '♦'

def display_card(card: dict) -> str:
    extra_space = ' '

    if len(card['rank']) == 2:
        extra_space = ''

    return f"{card['rank']} {extra_space}{display_suit_symbol(card['suit'])}"

def main() -> None:
    num_decks = 1
    num_players = 1

    shoe_cards = get_shoe_cards(num_decks)
    
    # TODO: player class with cards and chip count

    players = []

    for i in range(0, num_players):
        players.append({
            'chips': 100,
            'cards': [],
        })

    dealer = {
        'chips': 1000000,
        'cards': [],
    }

    for j in range(0, 2):
        for i in range(0, num_players):
            players[i]['cards'].append(shoe_cards.pop(0))

        dealer['cards'].append(shoe_cards.pop(0))

    print(len(shoe_cards))




    



    return
    print(len(shoe_cards))
    for shoe_card in shoe_cards[0:20]:
        print(display_card(shoe_card))

    card = shoe_cards.pop(0)

    print()
    print(display_card(card))
    print()

    print(display_card(shoe_cards[0]))

if __name__ == '__main__':
    main()
