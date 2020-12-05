from os import path

def load_input(filename):
    input_data = ""
    with open(path.join("input", filename)) as fd:
        input_data = fd.read()
    return input_data