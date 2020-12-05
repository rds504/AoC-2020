from tools.general import load_input

def count_trees(tree_map, slope):

    trees  = 0
    rows   = len(tree_map)
    cols   = len(tree_map[0])
    x,y    = 0,0
    dx, dy = slope

    while y < rows:
        if tree_map[y][x] == '#':
            trees += 1
        x = (x + dx) % cols
        y += dy

    return trees

def prod_slopes(tree_map, slopes):

    product = 1

    for slope in slopes:
        product *= count_trees(tree_map, slope)

    return product

input_data = load_input("day3.txt").split('\n')

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

for i in range(len(slopes)):
    print(f"Part {i + 1} => {prod_slopes(input_data, slopes[i])}")
