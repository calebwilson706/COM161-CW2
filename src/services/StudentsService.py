from src.utils.files.CreateFileIfItDoesNotExist import create_file_if_it_does_not_exist
from src.models.student.Student import Student


class StudentsService:
    def __init__(self, students_file_path):
        self.students_file_path = students_file_path

        create_file_if_it_does_not_exist(students_file_path)

    def output_all_with_summary(self):
        # output prettily
        print(self.get_students_from_file())

    def get_students_from_file(self):
        # deal with errors
        students_file = open(self.students_file_path, "r")
        result = []

        for line in students_file:
            result.append(
                Student.build_from_string(line)
            )

        return result

