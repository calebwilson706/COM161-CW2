from statistics import mean
from src.utils.files.CreateFileIfItDoesNotExist import create_file_if_it_does_not_exist
from src.utils.inputs.GetInputThatMatchesPredicate import get_input_that_matches_predicate
from src.utils.outputs.success.PrintSuccess import print_success
from src.utils.outputs.warn.PrintWarn import print_warn
from src.models.student.Student import Student
from collections import defaultdict


class StudentsService:
    def __init__(self, students_file_path):
        self.students_file_path = students_file_path

        create_file_if_it_does_not_exist(students_file_path)

        self.students = self.get_students_from_file()

    def output_all_students_with_summary(self):
        self.output_student_list()
        self.output_student_count_summary()

        print()

    def get_students_from_file(self):
        students_file = open(self.students_file_path, "r")
        result = []

        for line in students_file:
            if student := Student.build_from_string(line): result.append(student)

        students_file.close()

        return result

    def output_student_list(self):
        print("All Students:")

        for student in self.students:
            print("-", student.build_string_for_display())

    def output_student_count_summary(self):
        print("\nSummary:")
        print("The total amount of student(s) is", len(self.students))

        for country, students_in_country in self.students_grouped_by_country().items():
            print("-", len(students_in_country), "from", country)

    def students_grouped_by_country(self):
        result = defaultdict(list)

        for student in self.students:
            result[student.country].append(student)

        return result

    def output_details_of_youngest_and_oldest_students(self):
        students = self.get_students_from_file()

        if len(students) == 0:
            print_warn("Whoops! There are no students in the file.\n")
            return

        youngest = self.get_youngest_student()
        oldest = self.get_oldest_student()

        youngest.display_details("The youngest student:")
        oldest.display_details("The oldest student:")

        print()

    def get_youngest_student(self) -> Student:
        return min(self.students, key=lambda student: student.age)

    def get_oldest_student(self) -> Student:
        return max(self.students, key=lambda student: student.age)

    def add_new_student(self):
        new_student = StudentsService.input_new_students_details()

        self.append_student_to_file(
            new_student
        )
        self.students.append(new_student)

        print_success("The student has been added!")
        print_success(f'-> there is now {self.count_students_in_file()} students in the file.')
        print_success(f'-> the student\'s age is {new_student.age} which is {self.get_difference_between_age_and_average(new_student)} the average age.')

    @staticmethod
    def input_new_students_details() -> Student:
        student_number = get_input_that_matches_predicate(
            "Enter the students number: ",
            lambda x: x[0] == "B" and len(x) == 4,
            "Whoops! The student number must start with 'B' and be 4 characters long, please try again..."
        )
        first_names = input("Enter the first name(s) of the student: ")
        surname = input("Enter the surname of the student: ")
        age = int(get_input_that_matches_predicate(
            "Enter the age of the student: ",
            lambda x: x.isdigit(),
            "Whoops! that doesn't look like a valid age"
        ))
        country = input("Please enter the country of origin of the student: ")

        return Student(student_number, surname, first_names, age, country)

    def append_student_to_file(self, student):
        students_file = open(self.students_file_path, "a")

        students_file.write(student.build_string_for_storage() + "\n")

        students_file.close()

    def count_students_in_file(self):
        return len(self.students)

    def get_difference_between_age_and_average(self, student):
        average = self.get_average_age_of_students_in_file()

        difference = student.age - average

        if difference < 0:
            return f'{abs(difference)} below'
        elif difference > 0:
            return f'{difference} above'
        else:
            return "the same as"

    def get_average_age_of_students_in_file(self):
        return mean(
            map(
                lambda s: s.age,
                self.students
            )
        )
