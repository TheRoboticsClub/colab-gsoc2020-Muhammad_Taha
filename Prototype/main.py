import ctypes
import numpy as np
import multiprocessing

# Reads path from provided arguments and loads files
def initialize():

    import argparse
    parser = argparse.ArgumentParser(description='Python Synthesizer')
    parser.add_argument('--mapping', help='Enter path to mapping.json', default="examples/mapping.json")
    args = parser.parse_args()

    data = load_JSON(args.mapping)

    return data

# Loads JSON object created by NodeJS frontend
def load_JSON(file_path):

    import json
    with open(file_path) as obj:
        data = json.load(obj)
    return data


if __name__ == "__main__":

    data = initialize()

    processes = []
    for i, element in enumerate(data["mapping"]):

        from importlib import import_module
        method_name = 'modules.' + element["block_name"] + '.' + element["block_name"]
        module, function = method_name.rsplit('.',1)
        mod = import_module(module)
        method = getattr(mod, function)

        input_args = element["input_wires"]
        output_args = element["output_wires"]
        parameters = element["parameters"]

        processes.append(multiprocessing.Process(target=method,
        args=(input_args, output_args, parameters,)))

        processes[i].start()
