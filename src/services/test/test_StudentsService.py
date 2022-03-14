from unittest import TestCase
from unittest.mock import patch, call, MagicMock
from src.services.StudentsService import StudentsService
from src.models.student.Student import Student

caleb = Student("B000", "Wilson", "Caleb", 19, "NI")
bob = Student("B001", "McBobberson", "Bob", 19, "England")
lewis = Student("B002", "Hamilton", "Lewis", 38, "England")

fake_file = MagicMock()


class TestStudentsService(TestCase):
    @patch("builtins.open", return_value=fake_file)
    def test_get_students_from_file_closes(self, _):
        target = StudentsService("data/mock.txt")

        target.get_students_from_file()

        fake_file.close.assert_called_once()

    def test_get_students_from_file(self):
        target = StudentsService("data/mock.txt")

        result = target.get_students_from_file()

        self.assertEqual(
            [caleb, bob, lewis],
            result
        )

    @patch("builtins.input")
    @patch("src.services.StudentsService.StudentsService.output_student_list")
    @patch("src.services.StudentsService.StudentsService.output_student_count_summary")
    def test_output_all_students_with_summary(self, mock_scs, mock_sl, _):
        target = StudentsService("data/mock.txt")

        target.output_all_students_with_summary()

        mock_scs.assert_called_with([caleb, bob, lewis])
        mock_sl.assert_called_with([caleb, bob, lewis])

    @patch("builtins.print")
    def test_output_student_list(self, mock):
        StudentsService.output_student_list([caleb, bob])

        mock.assert_has_calls([
            call('-', 'Caleb Wilson (B000). 19 years old from NI.'),
            call('-', 'Bob McBobberson (B001). 19 years old from England.')
        ])

    @patch("builtins.print")
    def test_output_student_count_summary(self, mock):
        StudentsService.output_student_count_summary([caleb, bob, lewis])

        mock.assert_has_calls([
            call("The total amount of student(s) is", 3),
            call("-", 1, "from", "NI"),
            call("-", 2, "from", "England")
        ])

    def test_group_students_by_country(self):
        result = StudentsService.group_students_by_country([caleb, bob, lewis])

        self.assertEqual(
            {"NI": [caleb], "England": [bob, lewis]},
            result
        )

