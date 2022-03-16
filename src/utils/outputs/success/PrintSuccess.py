from src.utils.outputs.PrintColoured import print_coloured


def print_success(*message):
    print_coloured("\u001b[32m", *message)
