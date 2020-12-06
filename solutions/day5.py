from tools.general import load_input

def resolve_bsp(bsp_code, low_char, high_char):

    lower = 0
    upper = 2 ** len(bsp_code) - 1

    for c in bsp_code:
        mid = (lower + upper) // 2
        if c == high_char:
            lower = mid + 1
        elif c == low_char:
            upper = mid
        else:
            raise ValueError(f"Invalid character '{c}'")

    return lower

def seat_id(bp_code):

    row = resolve_bsp(bp_code[:7], 'F', 'B')
    col = resolve_bsp(bp_code[7:], 'L', 'R')

    return (8 * row) + col

taken_seats = sorted(seat_id(s) for s in load_input("day5.txt").split('\n'))

print(f"Part 1 => {taken_seats[-1]}")

prev = taken_seats[0]
for s in taken_seats[1:]:
    if 2 == (s - prev):
        print(f"Part 2 => {s - 1}")
        break
    prev = s
