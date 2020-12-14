import re
from tools.general import load_input_list

def set_bit(original, bit):
    return original | (1 << bit)

def unset_bit(original, bit):
    return original & ~(1 << bit)

def apply_bitmask_to_value(mask, original):

    for bit, val in enumerate(mask[::-1]):
        if val == '1':
            original = set_bit(original, bit)
        elif val == '0':
            original = unset_bit(original, bit)

    return original

def apply_bitmask_to_address(mask, original):

    results = [original]

    for bit, val in enumerate(mask[::-1]):
        if val == '1':
            results = [set_bit(r, bit) for r in results]
        elif val == 'X':
            results = [set_bit(r, bit) for r in results] + [unset_bit(r, bit) for r in results]

    return results

def run_docking_program(program, chip_ver=1):

    bitmask_pattern  = re.compile("^mask = ([01X]{36})$")
    writemem_pattern = re.compile("^mem\[([0-9]+)\] = ([0-9]+)$")

    bitmask = ""
    mem_map = {}

    for line in program:

        match = bitmask_pattern.match(line)
        if match:
            bitmask = match.group(1)
            continue

        match = writemem_pattern.match(line)
        if not match:
            raise ValueError(f"Invalid instruction: {line}")

        if chip_ver == 1:
            mem_map[int(match.group(1))] = apply_bitmask_to_value(bitmask, int(match.group(2)))
        else: # chip_ver == 2
            value = int(match.group(2))
            for addr in apply_bitmask_to_address(bitmask, int(match.group(1))):
                mem_map[addr] = value

    return sum(mem_map.values())

docking_program = load_input_list("day14.txt")

print(f"part 1 => {run_docking_program(docking_program)}")
print(f"part 2 => {run_docking_program(docking_program, 2)}")
