from src.utils.files.CreateFileIfItDoesNotExist import create_file_if_it_does_not_exist
from src.models.student.Student import Student
from collections import defaultdict


class StudentsService:
    def __init__(self, students_file_path):
        self.students_file_path = students_file_path

        create_file_if_it_does_not_exist(students_file_path)

    def output_all_students_with_summary(self):
        students = self.get_students_from_file()

        StudentsService.output_student_list(students)
        StudentsService.output_student_count_summary(students)

    def get_students_from_file(self):
        # deal with errors + test
        students_file = open(self.students_file_path, "r")
        result = []

        for line in students_file:
            result.append(
                Student.build_from_string(line)
            )

        students_file.close()

        return result

    @staticmethod
    def output_student_list(students):
        print("All Students:")

        for student in students:
            print("-", student.build_string_for_display())

    @staticmethod
    def output_student_count_summary(students):
        print("\nSummary:")
        print("The total amount of student(s) is", len(students))

        for country, students_in_country in StudentsService.group_students_by_country(students).items():
            print("-", len(students_in_country), "from", country)

    @staticmethod
    def group_students_by_country(students):
        result = defaultdict(list)

        for student in students:
            result[student.country].append(student)

        return result
