import re
from tools.general import load_input_list

input_data = load_input_list("day2.txt")
pattern    = re.compile("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")

valid_p1, valid_p2 = 0, 0
for i in input_data:

    m = pattern.match(i)
    if m:
        lower    = int(m.group(1))
        upper    = int(m.group(2))
        char     = m.group(3)
        password = m.group(4)

        # Part 1
        if lower <= password.count(char) <= upper:
            valid_p1 += 1

        # Part 2
        if char == password[lower - 1]:
            if char != password[upper - 1]:
                valid_p2 += 1
        elif char == password[upper - 1]:
            valid_p2 += 1

print(f"Part 1 => {valid_p1}")
print(f"Part 2 => {valid_p2}")
