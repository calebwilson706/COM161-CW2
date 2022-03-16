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

        fake_file.close.assert_called()

    def test_get_students_from_file(self):
        target = StudentsService("data/mock.txt")

        result = target.get_students_from_file()

        self.assertEqual(
            [caleb, bob, lewis],
            result
        )

    @patch("src.models.student.Student.Student.display_error_for_failed_build_from_string")
    def test_get_students_from_file_with_invalid(self, mock):
        target = StudentsService("data/mock-with-fail.txt")

        result = target.get_students_from_file()

        self.assertEqual(
            [caleb, bob, lewis],
            result
        )
        mock.assert_has_calls([
            call("B003, Mazepin, Nikita, Russia", "Not correct amount of attributes in string"),
            call("B004, Mazepin, Nikita, x, Russia", "invalid literal for int() with base 10: 'x'")
        ])

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

    @patch("src.services.StudentsService.StudentsService.get_students_from_file", return_value=[])
    @patch("src.services.StudentsService.print_warn")
    @patch("src.services.StudentsService.StudentsService.get_youngest_student")
    def test_output_details_of_youngest_and_oldest_students_terminates_when_empty_list(self, mock_get_youngest, mock_print, _):
        target = StudentsService("data/mock.txt")

        target.output_details_of_youngest_and_oldest_students()

        mock_print.assert_called_once_with("Whoops! There are no students in the file.\n")
        mock_get_youngest.assert_not_called()

    @patch("builtins.print")
    def test_output_details_of_youngest_and_oldest_students(self, mock_print):
        target = StudentsService("data/mock.txt")

        target.output_details_of_youngest_and_oldest_students()

        mock_print.assert_has_calls([
            call("The youngest student:"),
            call("-", caleb.build_string_for_display()),
            call("The oldest student:"),
            call("-", lewis.build_string_for_display())
        ])

    def test_get_youngest_student(self):
        result = StudentsService.get_youngest_student([caleb, bob, lewis])

        self.assertEqual(
            result,
            caleb
        )

    def test_get_oldest_student(self):
        result = StudentsService.get_oldest_student([caleb, bob, lewis])

        self.assertEqual(
            result,
            lewis
        )

    @patch("builtins.open", return_value=fake_file)
    def test_append_student_to_file(self, mock):
        target = StudentsService("data/mock.txt")

        target.append_student_to_file(bob)

        fake_file.write.assert_called_with(
            "B001, McBobberson, Bob, 19, England\n"
        )
        fake_file.close.assert_called_once()

    @patch("builtins.input", side_effect=[
        "B000",
        "Caleb",
        "Wilson",
        "19",
        "NI"
    ])
    def test_input_new_students_details(self, mock_input):
        result = StudentsService.input_new_students_details()

        self.assertEqual(
            caleb,
            result
        )

    def test_count_students_in_file(self):
        target = StudentsService("data/mock.txt")

        result = target.count_students_in_file()

        self.assertEqual(
            result,
            3
        )

    def test_difference_between_larger_age_and_average(self):
        target = StudentsService("data/mock.txt")

        result = target.get_difference_between_age_and_average(
            lewis
        )

        self.assertEqual(
            f'{38 - 76/3} above',
            result
        )

    def test_difference_between_lower_age_and_average(self):
        target = StudentsService("data/mock.txt")

        result = target.get_difference_between_age_and_average(
            caleb
        )

        self.assertEqual(
            f'{abs(76/3 - 19)} below',
            result
        )

    def test_difference_between_same_age_and_average(self):
        target = StudentsService("data/mock.txt")

        result = target.get_difference_between_age_and_average(
            Student(
                "B000",
                "C",
                "W",
                76/3,
                "USA"
            )
        )

        self.assertEqual(
            "the same as",
            result
        )

    def test_get_average_age_of_students_in_file(self):
        target = StudentsService("data/mock.txt")

        result = target.get_average_age_of_students_in_file()

        self.assertEqual(
            result,
            76/3
        )
