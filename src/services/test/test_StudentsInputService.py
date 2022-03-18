from unittest import TestCase
from unittest.mock import patch
from src.models.student.Student import Student
from src.services.StudentsInputService import StudentsInputService

caleb = Student("B000", "Wilson", "Caleb", 19, "NI")


class TestStudentsInputService(TestCase):
    @patch("builtins.input", side_effect=[
        "B000",
        "Caleb",
        "Wilson",
        "19",
        "NI"
    ])
    def test_input_new_students_details(self, mock_input):
        result = StudentsInputService.input_new_students_details()

        self.assertEqual(
            caleb,
            result
        )
