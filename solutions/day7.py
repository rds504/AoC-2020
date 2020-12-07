import re
from tools.general import load_input

input_data = load_input("day7.txt").split('\n')

def colours_containing(colour_map, colour):

    containing = set()

    for i in colour_map:
        if colour in colour_map[i]:
            containing.add(i)
            containing.update(colours_containing(colour_map, i))

    return containing

def num_bags_contained(colour_map, colour):

    # Don't include this bag
    count = 0

    for i in colour_map[colour]:
        # Increment by 1 for every sub-bag, plus sub-sub-bags
        count += colour_map[colour][i] * (1 + num_bags_contained(colour_map, i))

    return count

outer_pattern = re.compile("^([a-z]+ [a-z]+) bags contain ([0-9a-z ,]+).$")
inner_pattern = re.compile("^([0-9]+) ([a-z]+ [a-z]+) bags?$")
colour_map    = {}

for rule in input_data:
    om = outer_pattern.match(rule)
    if om:
        sub_map = {}
        for i in om.group(2).split(", "):
            im = inner_pattern.match(i)
            if im:
                sub_map[im.group(2)] = int(im.group(1))
        colour_map[om.group(1)] = sub_map

print(f"Part 1 => {len(colours_containing(colour_map, 'shiny gold'))}")
print(f"Part 2 => {num_bags_contained(colour_map, 'shiny gold')}")
