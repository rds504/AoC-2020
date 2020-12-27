import re
from tools.general import load_input_list

def count_valid_passwords(password_data):

    pattern  = re.compile("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")
    valid_p1 = 0
    valid_p2 = 0

    for entry in password_data:

        match = pattern.match(entry)

        if not match:
            raise ValueError(f"Invalid entry: '{entry}'")

        lower  = int(match.group(1))
        upper  = int(match.group(2))
        char   = match.group(3)
        passwd = match.group(4)

        if lower <= passwd.count(char) <= upper:
            valid_p1 += 1

        if char == passwd[lower - 1]:
            if char != passwd[upper - 1]:
                valid_p2 += 1
        elif char == passwd[upper - 1]:
            valid_p2 += 1

    return valid_p1, valid_p2

valid_pt1, valid_pt2 = count_valid_passwords(load_input_list("day2.txt"))
print(f"Part 1 => {valid_pt1}")
print(f"Part 2 => {valid_pt2}")
