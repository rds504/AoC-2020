import re, tools.general

input_data     = tools.general.load_input("day2.txt").split('\n')
pattern        = re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")
valid1, valid2 = 0, 0

for i in input_data:

    m = pattern.match(i)
    if m:
        lower, upper, char, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)

        # Part 1
        if lower <= password.count(char) <= upper:
            valid1 += 1

        # Part 2
        if char == password[lower - 1]:
            if char != password[upper - 1]:
                valid2 += 1
        elif char == password[upper - 1]:
            valid2 += 1

print(f"Part 1 => {valid1}")
print(f"Part 2 => {valid2}")
