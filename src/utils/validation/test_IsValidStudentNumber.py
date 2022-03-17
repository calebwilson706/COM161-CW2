from unittest import TestCase
from src.utils.validation.IsValidStudentNumber import is_valid_student_number


class Test(TestCase):
    def test_is_valid_student_number_happy(self):
        self.assertTrue(
            is_valid_student_number("B000")
        )

    def test_is_valid_student_number_fail(self):
        for case in [
            "W000",
            "b000",
            "B00",
            ""
        ]:
            self.assertFalse(
                is_valid_student_number(case)
            )
