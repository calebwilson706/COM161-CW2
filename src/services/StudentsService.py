from collections import defaultdict
from statistics import mean
from typing import Optional
from matplotlib import pyplot as plt
from src.models.student.Student import Student
from src.services.StudentsInputService import StudentsInputService
from src.utils.files.CreateFileIfItDoesNotExist import create_file_if_it_does_not_exist
from src.utils.outputs.success.PrintSuccess import print_success
from src.utils.outputs.warn.PrintWarn import print_warn
# noinspection PyBroadException


class StudentsService:
    def __init__(self, students_file_path):
        try:
            self.students_file_path = students_file_path

            create_file_if_it_does_not_exist(students_file_path)

            self.students = self.get_students_from_file()
        except Exception as e:
            raise e

    def output_all_students_with_summary(self):
        self.output_all_students()
        self.output_student_count_summary()

        print()

    def get_students_from_file(self):
        try:
            students_file = open(self.students_file_path, "r")
            result = []

            for line in students_file:
                if student := Student.build_from_string(line): result.append(student)

            students_file.close()

            return result
        except Exception as e:
            raise e

    def output_all_students(self):
        print("All Students:")
        StudentsService.display_students_in_list(
            self.students
        )

    @staticmethod
    def display_students_in_list(students):
        for student in students:
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
        if len(self.students) == 0:
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
        try:
            new_student = StudentsInputService.input_new_students_details()

            self.append_student_to_file(
                new_student
            )
            self.students.append(new_student)

            print_success("The student has been added!")
            print_success(f'-> there is now {self.count_students_in_file()} students in the file.')
            print_success(f'-> the student\'s age is {new_student.age} which is {self.get_difference_between_age_and_average(new_student)} the average age.')
        except Exception as e:
            raise e

    def append_student_to_file(self, student):
        try:
            students_file = open(self.students_file_path, "a")

            students_file.write(student.build_string_for_storage() + "\n")

            students_file.close()
        except Exception as e:
            raise e

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

    def search_by_id(self):
        student_id = StudentsInputService.input_student_id()

        student = self.get_student_with_id(
            student_id
        )

        if unwrapped_student := student:
            print_success("Found student")
            print_success("-> ", unwrapped_student.build_string_for_display())
        else:
            print_warn(f'The student with id: {student_id} was not found')

        print()

    def get_student_with_id(self, student_id) -> Optional[Student]:
        return next(
            (s for s in self.students if s.student_id == student_id),
            None
        )

    def output_sorted_students(self, field):
        print(f'Students sorted by {field}:')
        StudentsService.display_students_in_list(
            sorted(self.students, key=lambda s: getattr(s, field))
        )
        print()

    def show_countries_bar_chart(self):
        grouped_by_countries = self.students_grouped_by_country()

        countries = list(grouped_by_countries.keys())
        students = list(map(lambda x: len(x), grouped_by_countries.values()))

        plt.bar(
            countries,
            students
        )

        plt.show()
