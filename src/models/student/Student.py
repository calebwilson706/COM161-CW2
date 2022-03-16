from src.utils.outputs.error.PrintError import print_error


class Student:
    attribute_count = 5

    def __init__(self, student_id: str, surname: str, forename: str, age: int, country: str):
        self.student_id = student_id
        self.surname = surname
        self.forename = forename
        self.age = age
        self.country = country

    def __eq__(self, other: "Student") -> bool:
        return (
            self.student_id == other.student_id
            and self.surname == other.surname
            and self.forename == other.forename
            and self.age == other.age
            and self.country == other.country
        )

    @classmethod
    def build_from_string(cls, string: str) -> "Student":
        stripped_string = string.strip()

        try:
            parts = stripped_string.split(", ")

            if len(parts) != cls.attribute_count:
                raise ValueError("Not correct amount of attributes in string")

            student_id, surname, forename, age, country = parts

            return cls(student_id, surname, forename, int(age), country)

        except Exception as error:
            Student.display_error_for_failed_build_from_string(stripped_string, str(error))

    @staticmethod
    def display_error_for_failed_build_from_string(string, error):
        print_error("Student failed to be read with error:")
        print_error("  ", error)
        print_error("   student text ->", string)
        print()

    def build_string_for_storage(self):
        return f'{self.student_id}, {self.surname}, {self.forename}, {self.age}, {self.country}'

    def build_string_for_display(self):
        return f'{self.forename} {self.surname} ({self.student_id}). {self.age} years old from {self.country}.'

    def display_details(self, title):
        print(title)
        print("-", self.build_string_for_display())
