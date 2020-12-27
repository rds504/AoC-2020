import re
from tools.general import load_input_list

def parse_bag_rules(bag_rule_list):

    outer_pattern  = re.compile("^([a-z]+ [a-z]+) bags contain ([0-9a-z ,]+).$")
    inner_pattern  = re.compile("^([0-9]+) ([a-z]+ [a-z]+) bags?$")
    colour_map = {}

    for rule in bag_rule_list:

        om = outer_pattern.match(rule)
        if om:
            sub_map = {}
            for i in om.group(2).split(", "):
                im = inner_pattern.match(i)
                if im:
                    sub_map[im.group(2)] = int(im.group(1))
            colour_map[om.group(1)] = sub_map

    return colour_map

def colours_containing(colour_map, colour):

    containing = set()

    for c in colour_map:
        if colour in colour_map[c]:
            containing.add(c)
            containing.update(colours_containing(colour_map, c))

    return containing

def num_bags_contained(colour_map, colour):

    # Don't include this bag
    count = 0

    for b in colour_map[colour]:
        # Increment by 1 for every sub-bag, plus (recursively) sub-sub-bags
        count += colour_map[colour][b] * (1 + num_bags_contained(colour_map, b))

    return count

bag_colour_map = parse_bag_rules(load_input_list("day7.txt"))
print(f"Part 1 => {len(colours_containing(bag_colour_map, 'shiny gold'))}")
print(f"Part 2 => {num_bags_contained(bag_colour_map, 'shiny gold')}")
