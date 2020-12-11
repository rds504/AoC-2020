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

def first_seat_state(seating_map, position, direction, one_step_only):

    x ,  y = position
    dx, dy = direction
    x1, y1 = x + dx, y + dy

    while (not one_step_only) and seating_map.get((x1,y1)) == SEAT_NONE:
        x1 += dx
        y1 += dy

    return seating_map.get((x1,y1))

def update_state(seating_map, position, max_nearby_occupied, one_step_only):

    if seating_map[position] == SEAT_NONE:
        return SEAT_NONE

    occupied = 0
    for direction in DIRECTION_VECTORS:
        if first_seat_state(seating_map, position, direction, one_step_only) == SEAT_OCCUPIED:
            occupied += 1

    if seating_map[position] == SEAT_EMPTY:
        if occupied == 0:
            return SEAT_OCCUPIED
        return SEAT_EMPTY

    if seating_map[position] == SEAT_OCCUPIED:
        if max_nearby_occupied <= occupied:
            return SEAT_EMPTY
        return SEAT_OCCUPIED

    return None

def resolve_map(seating_map, max_nearby_occupied, one_step_only):

    map_stable = False
    while not map_stable:

        new_map = {}
        map_stable = True

        for position in seating_map:

            old_state = seating_map[position]
            new_state = update_state(seating_map, position, max_nearby_occupied, one_step_only)

            if new_state != old_state:
                map_stable = False

            new_map[position] = new_state

        seating_map = new_map

    return seating_map

def count_occupied(seating_map):
    return sum(value == SEAT_OCCUPIED for value in seating_map.values())

input_map = load_input_map("day11.txt")

print(f"Part 1 => {count_occupied(resolve_map(input_map, 4, True))}")
print(f"Part 2 => {count_occupied(resolve_map(input_map, 5, False))}")
