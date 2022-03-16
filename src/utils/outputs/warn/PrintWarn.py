from src.utils.outputs.PrintColoured import print_coloured


def print_warn(*message):
    print_coloured("\033[93m", *message)
