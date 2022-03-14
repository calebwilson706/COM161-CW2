from unittest import TestCase

from src.models.student.Student import Student

valid_string = "B000, Wayne, Bruce, 25, USA"
valid_student = Student("B000", "Wayne", "Bruce", 25, "USA")

invalid_age_string = "B000, Wayne, Bruce, a, USA"
invalid_attribute_count_strings = [
    "a",
    "a ,b, c, d",
    "a, b, c, d, e, f"
]


class TestStudent(TestCase):
    def test_build_from_string(self):
        result = Student.build_from_string(valid_string)

        self.assertEqual(
            valid_student,
            result
        )

    def test_build_from_string_with_new_line(self):
        result = Student.build_from_string(valid_string + "\n")

        self.assertEqual(
            valid_student,
            result
        )

    def test_build_from_string_throws_error_when_age_is_not_valid(self):
        self.assert_raises_with_message(
            ValueError,
            lambda: Student.build_from_string(invalid_age_string),
            "invalid literal for int() with base 10: 'a'"
        )

    def test_build_from_string_throws_error_when_there_is_not_correct_attribute_count(self):
        for string in invalid_attribute_count_strings:
            self.assert_raises_with_message(
                ValueError,
                lambda: Student.build_from_string(string),
                "Not correct amount of attributes in string"
            )

    def test_build_string_for_storage(self):
        result = valid_student.build_string_for_storage()

        self.assertEqual(
            valid_string,
            result
        )

    def test_build_string_for_display(self):
        result = valid_student.build_string_for_display()

        self.assertEqual(
            "Bruce Wayne (B000). 25 years old from USA",
            result
        )

    def assert_raises_with_message(self, exception, callback, message):
        with self.assertRaises(exception) as context:
            callback()

        self.assertEqual(str(context.exception), message)
