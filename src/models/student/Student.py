class Student:
    attribute_count = 5

    def __init__(self, student_id: str, surname: str, forename: str, age: int, country: str):
        self.student_id = student_id
        self.surname = surname
        self.forename = forename
        self.age = age
        self.country = country

    def __eq__(self, other: "student") -> bool:
        return (
            self.student_id == other.student_id
            and self.surname == other.surname
            and self.forename == other.forename
            and self.age == other.age
            and self.country == other.country
        )

    @classmethod
    def build_from_string(cls, string: str) -> "student":
        try:
            parts = string.strip().split(", ")

            if len(parts) != cls.attribute_count:
                raise ValueError("Not correct amount of attributes in string")

            student_id, surname, forename, age, country = parts

            return cls(
                student_id,
                surname,
                forename,
                int(age),
                country
            )
        except Exception as e:
            raise e

    def build_string(self):
        return f'{self.student_id}, {self.surname}, {self.forename}, {self.age}, {self.country}'
