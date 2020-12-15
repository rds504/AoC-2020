from tools.general import load_input

def play_until(start_sequence, n_turns):

    last_term = start_sequence[-1]
    last_seen = {n : i for i, n in enumerate(start_sequence[:-1])}

    for turn in range(len(start_sequence) - 1, n_turns - 1):
        next_term = turn - last_seen.get(last_term, turn) # zero if not seen before
        last_seen[last_term] = turn
        last_term = next_term

    return last_term

starting_numbers = [int(i) for i in load_input("day15.txt").split(',')]

print(f"Part 1 => {play_until(starting_numbers, 2020)}")
print(f"Part 2 => {play_until(starting_numbers, 30000000)}")
