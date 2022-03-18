from src.models.student.Student import Student
from src.utils.inputs.GetInputThatMatchesPredicate import get_input_that_matches_predicate
from src.utils.inputs.GetNonEmptyInput import get_non_empty_input
from src.utils.validation.IsValidStudentNumber import is_valid_student_number


class StudentsInputService:
    @staticmethod
    def input_new_students_details() -> Student:
        student_id = StudentsInputService.input_student_id()
        first_names = get_non_empty_input("Enter the first name(s) of the student: ")
        surname = get_non_empty_input("Enter the surname of the student: ")
        age = int(get_input_that_matches_predicate(
            "Enter the age of the student: ",
            lambda x: x.isdigit(),
            "Whoops! that doesn't look like a valid age"
        ))
        country = get_non_empty_input("Please enter the country of origin of the student: ")

        return Student(student_id, surname, first_names, age, country)

    @staticmethod
    def input_student_id() -> str:
        return get_input_that_matches_predicate(
            "Enter the students number: ",
            is_valid_student_number,
            "Whoops! The student number must start with 'B' and be 4 characters long, please try again..."
        )
