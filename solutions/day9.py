from itertools import combinations
from tools.general import load_input_ints

def contains_pair_sum(sequence, target):

    for x, y in combinations(sequence, 2):
        if x + y == target:
            return True

    return False

xmas_data = load_input_ints("day9.txt")
weakness_sum = None
weakness_range = None

for i in range(25, len(xmas_data)):

    if not contains_pair_sum(xmas_data[i - 25:i], xmas_data[i]):
        weakness_sum = xmas_data[i]
        break

print(f"Part 1 => {weakness_sum}")

for i in range(len(xmas_data)):

    s = xmas_data[i]
    j = i

    while s < weakness_sum:
        j += 1
        s += xmas_data[j]

    if s == weakness_sum:
        weakness_range = xmas_data[i:j + 1]
        break

print(f"Part 2 => {min(weakness_range) + max(weakness_range)}")
