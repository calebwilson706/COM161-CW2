def is_valid_student_number(value):
    return value != "" and value[0] == "B" and len(value) == 4
