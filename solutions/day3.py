from functools import reduce
from operator import mul
from tools.general import load_input_list

def count_trees(tree_map, slope):

    trees  = 0
    rows   = len(tree_map)
    cols   = len(tree_map[0])
    x, y   = 0,0
    dx, dy = slope

    while y < rows:
        if tree_map[y][x] == '#':
            trees += 1
        x = (x + dx) % cols
        y += dy

    return trees

input_data = load_input_list("day3.txt")

def prod_slopes(tree_map, slopes_list):
    return reduce(mul, (count_trees(tree_map, slope) for slope in slopes_list))

slopes = [
    [
        (3, 1)
    ],
    [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
]

for i, s in enumerate(slopes):
    print(f"Part {i + 1} => {prod_slopes(input_data, s)}")
