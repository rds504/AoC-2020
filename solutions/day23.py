from tools.arithmetic import product
from tools.general import load_input

def get_next_elements(linked_list, after, num):

    elements  = []
    next_elem = linked_list[after]

    for _ in range(num):
        elements.append(next_elem)
        next_elem = linked_list[next_elem]

    return elements

def play_crab_cups(initial_cup_sequence, iterations, max_cup, result_cups):

    # For fast shuffling of elements, a linked list is a good choice. In fact, a "proper"
    # linked list implementation is overkill here, we just need a map: node -> next node.
    next_cup = dict(zip(initial_cup_sequence, initial_cup_sequence[1:]))
    curr_cup = initial_cup_sequence[0]

    init_max = max(initial_cup_sequence)
    if init_max < max_cup:
        next_cup[initial_cup_sequence[-1]] = init_max + 1
        for i in range(init_max + 1, max_cup):
            next_cup[i] = i + 1
        next_cup[max_cup] = curr_cup
    else:
        next_cup[initial_cup_sequence[-1]] = curr_cup

    for _ in range(iterations):

        # Cut next 3 cups
        move_cups = get_next_elements(next_cup, curr_cup, 3)
        next_cup[curr_cup]  = next_cup[move_cups[-1]]

        destination = curr_cup
        while destination in [curr_cup] + move_cups:
            destination -= 1
            if destination == 0:
                destination = max_cup

        # Insert cut cups after destination
        next_cup[move_cups[-1]] = next_cup[destination]
        next_cup[destination]   = move_cups[0]

        curr_cup = next_cup[curr_cup]

    return get_next_elements(next_cup, 1, result_cups)

initial_cups = [int(c) for c in load_input("day23.txt")]

print(f"Part 1 => {''.join(str(c) for c in play_crab_cups(initial_cups, 100, 9, 8))}")
print(f"Part 2 => {product(play_crab_cups(initial_cups, 10**7, 10**6, 2))}")
