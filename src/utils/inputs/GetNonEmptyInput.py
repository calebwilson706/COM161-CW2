from src.utils.inputs.GetInputThatMatchesPredicate import get_input_that_matches_predicate


def get_non_empty_input(prompt):
    return get_input_that_matches_predicate(
        prompt,
        lambda x: x != ""
    )
