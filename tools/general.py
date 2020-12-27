from os import path
from typing import Dict, List, Tuple

def load_input(filename: str) -> str:

    input_data = ""

    with open(path.join("input", filename)) as file_handle:
        input_data = file_handle.read()

    return input_data

def load_input_list(filename: str) -> List[str]:
    return load_input(filename).split('\n')

def load_input_ints(filename: str) -> List[int]:
    return [int(i) for i in load_input_list(filename)]

def load_input_map(filename: str) -> Dict[Tuple[int, int], str]:

    input_map = {}

    for y, row in enumerate(load_input_list(filename)):
        for x, cell in enumerate(row):
            input_map[(x, y)] = cell

    return input_map
