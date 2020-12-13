import re
from tools.general import load_input_list

NORTH   = 'N'
EAST    = 'E'
SOUTH   = 'S'
WEST    = 'W'
LEFT    = 'L'
RIGHT   = 'R'
FORWARD = 'F'

DIRECTION_VECTOR = {
    NORTH : ( 0,  1),
    SOUTH : ( 0, -1),
    EAST  : ( 1,  0),
    WEST  : (-1,  0)
}

def move_point(point, direction, magnitude):
    px, py = point
    dx, dy = direction
    return (px + magnitude * dx, py + magnitude * dy)

def rotate_point(point, direction, degrees):

    if degrees % 90 != 0:
        raise ValueError(f"May only turn in 90 degree increments (tried {degrees})")

    x, y = point
    try:
        while degrees > 0:
            x, y = {
                LEFT  : (-y, x),
                RIGHT : (y, -x)
            }[direction]
            degrees -= 90
    except IndexError as ie:
        raise ValueError(
            f"May only turn LEFT ({LEFT}) or RIGHT ({RIGHT}) (tried {direction})"
        ) from ie

    return (x, y)

def navigate(instructions, use_waypoint=False):

    position = (0, 0)
    heading  = (10, 1) if use_waypoint else DIRECTION_VECTOR[EAST]
    pattern  = re.compile("^(N|S|E|W|L|R|F)([0-9]+)$")

    for instr in instructions:

        match = pattern.match(instr)
        if not match:
            raise ValueError(f"Invalid instruction \"{instr}\"")

        move = match.group(1)
        size = int(match.group(2))

        if move in (LEFT, RIGHT):
            heading  = rotate_point(heading, move, size)
        elif move == FORWARD:
            position = move_point(
                position,
                heading,
                size)
        elif use_waypoint:
            heading = move_point(
                heading,
                DIRECTION_VECTOR[move],
                size)
        else:
            position = move_point(
                position,
                DIRECTION_VECTOR[move],
                size)

    return position

def manhattan_dist(point):
    x, y = point
    return abs(x) + abs(y)

navigation_instr = load_input_list("day12.txt")
print(f"Part 1 => {manhattan_dist(navigate(navigation_instr))}")
print(f"Part 2 => {manhattan_dist(navigate(navigation_instr, True))}")
