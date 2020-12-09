from itertools import combinations
from functools import reduce
from operator import mul
from tools.general import load_input_ints

def find_tuple_with_sum(entry_list, target_sum, tuple_size):

    for combo in combinations(entry_list, tuple_size):
        if sum(combo) == target_sum:
            return combo

    return None

expense_entries = load_input_ints("day1.txt")
print(f"Part 1 => {reduce(mul, find_tuple_with_sum(expense_entries, 2020, 2))}")
print(f"Part 2 => {reduce(mul, find_tuple_with_sum(expense_entries, 2020, 3))}")
