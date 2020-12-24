from copy import deepcopy
from tools.general import load_input_list

DIRECTION_VECTORS = {
    "e"  : ( 1,  0),
    "ne" : ( 1, -1),
    "se" : ( 0,  1),
    "nw" : ( 0, -1),
    "sw" : (-1,  1),
    "w"  : (-1,  0)
}

def flip_tile(flipped_set, tile):
    if tile in flipped_set:
        flipped_set.remove(tile)
    else:
        flipped_set.add(tile)

def initialise_floor(instructions):

    flipped_tiles = set()

    for line in instructions:

        x, y = 0, 0
        sn_qual = ''

        for char in line:

            if char in "sn":
                sn_qual = char
                continue

            if char not in "ew":
                raise ValueError("Invalid direction '{char}'")

            dx, dy = DIRECTION_VECTORS[sn_qual + char]
            x, y = x + dx, y + dy
            sn_qual = ''

        flip_tile(flipped_tiles, (x, y))

    return flipped_tiles

def evolve_floor(initial_state, iterations):

    flipped_tiles = deepcopy(initial_state)

    for _ in range(iterations):

        xmin, xmax, ymin, ymax = 0, 0, 0, 0
        for x, y in flipped_tiles:
            xmin, xmax, ymin, ymax = min(xmin, x), max(xmax, x), min(ymin, y), max(ymax, y)

        to_flip = set()

        for x in range(xmin - 1, xmax + 2):
            for y in range(ymin - 1, ymax + 2):

                nbr_count = 0
                for dx, dy in DIRECTION_VECTORS.values():
                    if (x + dx, y + dy) in flipped_tiles:
                        nbr_count += 1

                if (x, y) in flipped_tiles:
                    if nbr_count == 0 or nbr_count > 2:
                        to_flip.add((x, y))
                elif nbr_count == 2:
                    to_flip.add((x, y))

        for tile in to_flip:
            flip_tile(flipped_tiles, tile)

    return flipped_tiles

initial_flipped_tiles = initialise_floor(load_input_list("day24.txt"))
print(f"Part 1 => {len(initial_flipped_tiles)}")
final_flipped_tiles = evolve_floor(initial_flipped_tiles, 100)
print(f"Part 2 => {len(final_flipped_tiles)}")
