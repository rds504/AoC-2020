from functools import reduce
from math import inf
from operator import mul
from tools.general import load_input_list

def find_first_bus(earliest, buses):

    first_bus, least_wait = None, inf

    for bus in buses:
        wait = bus - (earliest % bus)
        if wait < least_wait:
            first_bus, least_wait = bus, wait

    return first_bus, least_wait

# Extended Euclidean algorithm
def xgcd(opr1, opr2):

    x0, x1 = 0, 1
    y0, y1 = 1, 0

    while opr1 != 0:
        (q, opr1), opr2 = divmod(opr2, opr1), opr1
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1

    return opr2, x0

def mod_inverse(operand, modulus):

    gcd, inv = xgcd(operand, modulus)

    if gcd != 1:
        raise ValueError(f"{operand} and {modulus} are not coprime")

    return inv % modulus

# Chinese Remainder Theorem
#   Any sequence of pairs (c, m) where 0 <= c < m and all m are pairwise coprime defines a set of
#   simultaneous linear congruences with exactly one solution x satisfying 0 <= x < product(m).
def chinese_remainder(congruence_list):

    prod_m = reduce(mul, (m for c, m in congruence_list))
    solution = 0

    for c, m in congruence_list:
        p = prod_m // m
        solution = (solution + (m - c) * p * mod_inverse(p, m)) % prod_m

    return solution

earliest_dep, bus_schedule = load_input_list("day13.txt")
bus_array = {i : int(bus) for i, bus in enumerate(bus_schedule.split(',')) if bus != 'x'}

print(f"Part 1 => {reduce(mul, find_first_bus(int(earliest_dep), bus_array.values()))}")
print(f"Part 2 => {chinese_remainder(bus_array.items())}")
