from itertools import combinations
from tools.general import load_input_ints

def contains_pair_sum(sequence, target):

    for x, y in combinations(sequence, 2):
        if x + y == target:
            return True

    return False

def find_weakness(xmas_encrypted_data):

    weak_sum, weak_range = None, None

    for i, s in enumerate(xmas_encrypted_data[25:]):
        if not contains_pair_sum(xmas_encrypted_data[i:i + 25], s):
            weak_sum = s
            break

    for i, s in enumerate(xmas_encrypted_data):

        j = i
        while s < weak_sum:
            j += 1
            s += xmas_encrypted_data[j]

        if s == weak_sum:
            weak_range = xmas_encrypted_data[i:j + 1]
            break

    return weak_sum, weak_range

weakness_sum, weakness_range = find_weakness(load_input_ints("day9.txt"))
print(f"Part 1 => {weakness_sum}")
print(f"Part 2 => {min(weakness_range) + max(weakness_range)}")
