from os import path

def load_input(filename):

    input_data = ""

    with open(path.join("input", filename)) as file_handle:
        input_data = file_handle.read()

    return input_data
