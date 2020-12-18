from itertools import product
from tools.general import load_input_list

def get_new_active_range(current_active_set, dimensions):

    lowest    = [0] * dimensions
    highest   = [0] * dimensions

    for point in current_active_set:
        for i, coord in enumerate(point):
            if coord < lowest[i]:
                lowest[i] = coord
            elif highest[i] < coord:
                highest[i] = coord

    return tuple(range(lowest[i] - 1, highest[i] + 2) for i in range(dimensions))

def count_active_neighbours(active_set, point):

    active_count = 0

    for nbr in product(*(range(coord - 1, coord + 2) for coord in point)):
        if nbr in active_set and nbr != point:
            active_count += 1

    return active_count

def new_state_is_active(active_set, point):

    active_nbr = count_active_neighbours(active_set, point)

    if point in active_set:
        if 2 <= active_nbr <= 3:
            return True
    elif active_nbr == 3:
        return True

    return False

def iterate_grid(initial_grid, dimensions, iterations):

    active_points = set()

    for y, row in enumerate(initial_grid):
        for x, cube in enumerate(row):
            if cube == '#':
                active_points.add(tuple([x, y] + [0] * (dimensions - 2)))

    for _ in range(iterations):

        new_active_points = set()

        for point in product(*get_new_active_range(active_points, dimensions)):
            if new_state_is_active(active_points, point):
                new_active_points.add(point)

        active_points = new_active_points

    return len(active_points)

starting_grid = [list(row) for row in load_input_list("day17.txt")]

print(f"Part 1 => {iterate_grid(starting_grid, 3, 6)}")
print(f"Part 1 => {iterate_grid(starting_grid, 4, 6)}")
