from unittest import TestCase
from unittest.mock import patch
from CreateFileIfItDoesNotExist import create_file_if_it_does_not_exist


class Test(TestCase):
    @patch("builtins.open")
    def test_should_create_file(self, mock_open):
        create_file_if_it_does_not_exist("foo.txt")

        mock_open.assert_called_with("foo.txt", "x")

    @patch("CreateFileIfItDoesNotExist.isfile", return_value=True)
    @patch("builtins.open")
    def test_should_not_create_file(self, mock_open, _):
        create_file_if_it_does_not_exist("foo.txt")

        mock_open.assert_not_called()

