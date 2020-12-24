from tools.general import load_input

def parse_decks(input_data):
    return tuple([int(c) for c in deck.split('\n')[1:]] for deck in input_data.split("\n\n"))

def compute_score(deck):
    return sum(i * c for i, c in enumerate(deck[::-1], 1))

def play_hand(player1, player2, card1, card2):

    if card1 < card2:
        player2 += [card2, card1]
    elif card2 < card1:
        player1 += [card1, card2]
    else:
        raise ValueError("Ties are not expected")

def play_combat(player1_deck, player2_deck):

    player1, player2 = list(player1_deck), list(player2_deck)

    while len(player1) > 0 and len(player2) > 0:
        c1, c2 = player1.pop(0), player2.pop(0)
        play_hand(player1, player2, c1, c2)

    if len(player1) > 0:
        return 1, compute_score(player1)

    return 2, compute_score(player2)

def play_recursive_combat(player1_deck, player2_deck):

    player1, player2 = list(player1_deck), list(player2_deck)
    previous_decks = set()

    while len(player1) > 0 and len(player2) > 0:

        snapshot = (tuple(player1), tuple(player2))
        if snapshot in previous_decks:
            # Player 1 instantly wins
            return 1, compute_score(player1)
        previous_decks.add(snapshot)

        c1, c2 = player1.pop(0), player2.pop(0)

        if c1 <= len(player1) and c2 <= len(player2):
            # Recurse
            sub_winner, _ = play_recursive_combat(player1[:c1], player2[:c2])
            if sub_winner == 1:
                player1 += [c1, c2]
            else:
                player2 += [c2, c1]
        else:
            play_hand(player1, player2, c1, c2)

    if len(player1) > 0:
        return 1, compute_score(player1)

    return 2, compute_score(player2)

deck1, deck2 = parse_decks(load_input("day22.txt"))

print(f"Part 1 => {play_combat(deck1, deck2)[1]}")
print(f"Part 2 => {play_recursive_combat(deck1, deck2)[1]}")
