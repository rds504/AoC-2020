from functools import reduce
from math import inf
from operator import mul
from tools.general import load_input_list

puzzle_input = load_input_list("day13.txt")

# Part 1
earliest   = int(puzzle_input[0])
first_bus  = None
least_wait = inf
for bus in puzzle_input[1].split(','):
    if bus != 'x':
        bus = int(bus)
        wait = bus - (earliest % bus)
        if wait < least_wait:
            first_bus  = bus
            least_wait = wait
print(f"Part 1 => {first_bus * least_wait}")

# Part 2

# Extended Euclidean algorithm
def xgcd(a, b):

    x0, x1 = 0, 1
    y0, y1 = 1, 0

    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1

    return b, x0

def mod_inverse(a, m):

    gcd, inv = xgcd(a, m)

    if gcd != 1:
        raise ValueError(f"{a} and {m} are not coprime")

    return inv % m

# Chinese Remainder Theorem
#   Given a sequence of pairs (c, m) such that 0 <= c < m and all m are pairwise coprime, then there
#   is exactly one x satisfying 0 <= x < product(m) and x is congruent to c modulo m for all (c, m).
def chinese_remainder(congruence_list):

    prod = reduce(mul, (m for c, m in congruence_list))
    rem  = 0

    for c, m in congruences:
        p = prod // m
        rem = (rem + (m - c) * p * mod_inverse(p, m)) % prod

    return rem

congruences = [(i, int(bus)) for i, bus in enumerate(puzzle_input[1].split(',')) if bus != 'x']
print(f"Part 2 => {chinese_remainder(congruences)}")
