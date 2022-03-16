from typing import Optional, Callable
from src.utils.outputs.warn.PrintWarn import print_warn


def get_input_that_matches_predicate(
        prompt: str,
        predicate: Callable[[str], bool],
        warning: Optional[str] = None
):
    while True:
        value = input(prompt)

        if predicate(value):
            return value

        if warning is not None:
            print_warn(warning)
