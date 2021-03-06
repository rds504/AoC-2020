from os import path

def load_input(filename):

    input_data = ""

    with open(path.join("input", filename)) as file_handle:
        input_data = file_handle.read()

    return input_data

def load_input_list(filename):
    return load_input(filename).split('\n')

def load_input_ints(filename):
    return [int(i) for i in load_input_list(filename)]

def load_input_map(filename):

    input_map = {}

    for y, row in enumerate(load_input_list(filename)):
        for x, cell in enumerate(row):
            input_map[(x, y)] = cell

    return input_map
