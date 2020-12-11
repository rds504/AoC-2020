from tools.general import load_input_map

SEAT_EMPTY    = 'L'
SEAT_OCCUPIED = '#'
SEAT_NONE     = '.'

DIRECTION_VECTORS = (
    (-1, -1), # up + left
    ( 0, -1), # up
    ( 1, -1), # up + right
    (-1,  0), # left
    ( 1,  0), # right
    (-1,  1), # down + left
    ( 0,  1), # down
    ( 1,  1), # down + right
)

def count_occupied_nearby(seating_map, position, adjacent_only):

    occupied = 0
    x, y = position

    for dx, dy in DIRECTION_VECTORS:

        x1, y1 = x + dx, y + dy

        if not adjacent_only:
            while seating_map.get((x1,y1)) == SEAT_NONE:
                x1, y1 = x1 + dx, y1 + dy

        if seating_map.get((x1,y1)) == SEAT_OCCUPIED:
            occupied += 1

    return occupied

def update_cell(seating_map, position, max_nearby_occupied, adjacent_only):

    if seating_map[position] == SEAT_NONE:
        return SEAT_NONE

    occupied = count_occupied_nearby(seating_map, position, adjacent_only)

    if seating_map[position] == SEAT_EMPTY:
        if occupied == 0:
            return SEAT_OCCUPIED
        return SEAT_EMPTY

    if seating_map[position] == SEAT_OCCUPIED:
        if max_nearby_occupied <= occupied:
            return SEAT_EMPTY
        return SEAT_OCCUPIED

    return None

def resolve_map(seating_map, max_nearby_occupied, adjacent_only):

    while True:

        new_map = {
            position : update_cell(seating_map,
                                   position,
                                   max_nearby_occupied,
                                   adjacent_only)
            for position in seating_map
        }

        if new_map == seating_map:
            break

        seating_map = new_map

    return seating_map

def count_occupied(seating_map):
    return sum(value == SEAT_OCCUPIED for value in seating_map.values())

input_map = load_input_map("day11.txt")

print(f"Part 1 => {count_occupied(resolve_map(input_map, 4, True))}")
print(f"Part 2 => {count_occupied(resolve_map(input_map, 5, False))}")
