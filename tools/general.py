from os import path

def load_input(filename):

    input_data = ""

    with open(path.join("input", filename)) as fd:
        input_data = fd.read()

    return input_data

def load_input_list(filename):
    return load_input(filename).split('\n')

def load_input_ints(filename):
    return [int(i) for i in load_input_list(filename)]
