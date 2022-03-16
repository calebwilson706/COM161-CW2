from src.utils.outputs.PrintColoured import print_coloured


def print_error(*message):
    print_coloured("\033[91m", *message)
