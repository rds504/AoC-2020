import re
from itertools import product
from tools.general import load_input_list

class BitmaskV1:

    def __init__(self, mask):
        self._and_mask = int(mask.replace('X', '1'), 2)
        self._or_mask  = int(mask.replace('X', '0'), 2)

    def apply(self, value):
        return (value & self._and_mask) | self._or_mask

class BitmaskV2:

    def __init__(self, mask):
        self._masks = list(zip(
            (int(''.join(p), 2) for p in product(*('01' if b == 'X' else '1' for b in mask))),
            (int(''.join(p), 2) for p in product(*('01' if b == 'X' else   b for b in mask)))
        ))

    def apply(self, value):
        return ((value & and_mask) | or_mask for and_mask, or_mask in self._masks)

def run_docking_program(program, chip_ver2 = False):

    bitmask_pattern  = re.compile(r"^mask = ([01X]{36})$")
    writemem_pattern = re.compile(r"^mem\[([0-9]+)\] = ([0-9]+)$")

    bitmask = None
    mem_map = {}

    for line in program:

        match = bitmask_pattern.match(line)
        if match:
            bitmask = (BitmaskV2 if chip_ver2 else BitmaskV1)(match.group(1))
            continue

        match = writemem_pattern.match(line)
        if not match:
            raise ValueError(f"Invalid instruction: {line}")

        if chip_ver2:
            value = int(match.group(2))
            for addr in bitmask.apply(int(match.group(1))):
                mem_map[addr] = value
        else:
            mem_map[int(match.group(1))] = bitmask.apply(int(match.group(2)))

    return sum(mem_map.values())

docking_program = load_input_list("day14.txt")

print(f"part 1 => {run_docking_program(docking_program)}")
print(f"part 2 => {run_docking_program(docking_program, 2)}")
