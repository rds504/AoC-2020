import re
from tools.general import load_input_list

def run_program(program_code, swap_instr=None):

    accumulator   = 0
    current_instr = 0
    end_instr     = len(program_code)
    terminated    = False
    instrs_run    = set()
    instr_pattern = re.compile("^(acc|jmp|nop) ([+-])([0-9]+)$")

    while (not terminated) and (current_instr not in instrs_run):

        instrs_run.add(current_instr)
        instr_match = instr_pattern.match(program_code[current_instr])

        if not instr_match:
            raise ValueError(f"Invalid instruction: \"{program_code[current_instr]}\"")

        opr = instr_match.group(1)
        sgn = instr_match.group(2)
        arg = int(instr_match.group(3))

        if sgn == '-':
            arg *= -1

        if swap_instr == current_instr:
            opr = {
                "acc" : "acc",
                "jmp" : "nop",
                "nop" : "jmp"
            }[opr]

        action = {
            "acc" : lambda pos, acc, arg : (pos + 1  , acc + arg),
            "jmp" : lambda pos, acc, arg : (pos + arg, acc      ),
            "nop" : lambda pos, acc, arg : (pos + 1  , acc      )
        }[opr]

        current_instr, accumulator = action(current_instr, accumulator, arg)

        if current_instr == end_instr:
            terminated = True

    return (terminated, accumulator)

code = load_input_list("day8.txt")

print(f"Part 1 => {run_program(code)[1]}")

for swap_line in range(len(code)):
    terms, accum = run_program(code, swap_line)
    if terms:
        print(f"Part 2 => {accum}")
