from unittest import TestCase
from unittest.mock import patch
from src.utils.inputs.GetInputThatMatchesPredicate import get_input_that_matches_predicate


class Test(TestCase):
    @patch("builtins.input", return_value="a")
    def test_get_input_that_matches_predicate_returns_first_answer(self, mock_input):
        value = get_input_that_matches_predicate("", lambda x: x == "a")

        self.assertEqual(
            value,
            "a"
        )
        mock_input.assert_called_once()

    @patch("builtins.input", side_effect=["b", "a"])
    @patch("src.utils.inputs.GetInputThatMatchesPredicate.print_warn")
    def test_get_input_that_matches_predicate_returns_first_valid_answer(self, mock_print, mock_input):
        value = get_input_that_matches_predicate("", lambda x: x == "a")

        self.assertEqual(
            value,
            "a"
        )
        self.assertEqual(
            mock_input.call_count,
            2
        )
        mock_print.assert_not_called()

    @patch("builtins.input", side_effect=["b", "a"])
    @patch("src.utils.inputs.GetInputThatMatchesPredicate.print_warn")
    def test_get_input_that_matches_predicate_displays_warning(self, mock_print, mock_input):
        get_input_that_matches_predicate("", lambda x: x == "a", "warning")

        mock_print.assert_called_once_with("warning")
