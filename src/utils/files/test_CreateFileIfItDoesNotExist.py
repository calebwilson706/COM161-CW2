from unittest import TestCase
from unittest.mock import patch, MagicMock
from CreateFileIfItDoesNotExist import create_file_if_it_does_not_exist

fake_file = MagicMock()


class Test(TestCase):
    @patch("builtins.open", return_value=fake_file)
    def test_should_create_file(self, mock_open):
        create_file_if_it_does_not_exist("foo.txt")

        mock_open.assert_called_with("foo.txt", "x")
        fake_file.close.assert_called_once()

    @patch("CreateFileIfItDoesNotExist.isfile", return_value=True)
    @patch("builtins.open")
    def test_should_not_create_file(self, mock_open, _):
        create_file_if_it_does_not_exist("foo.txt")

        mock_open.assert_not_called()

