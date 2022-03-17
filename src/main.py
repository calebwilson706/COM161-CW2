from simple_term_menu import TerminalMenu
from src.services.StudentsService import StudentsService


class Options:
    output_all_details = "Output all students details and a summary"
    output_youngest_and_oldest_details = "Output the details of the youngest and oldest student"
    add_new_student = "Add a new student to the file"
    search_for_student_by_id = "Search for a student by their student number"
    exit = "Exit the program"


def main():
    options = [
        Options.output_all_details,
        Options.output_youngest_and_oldest_details,
        Options.add_new_student,
        Options.search_for_student_by_id,
        Options.exit
    ]

    students_service = StudentsService("data/students.txt")

    while True:
        menu = TerminalMenu(options)

        selected_option = options[menu.show()]

        print("You have selected:", selected_option, "\n")

        if selected_option == Options.output_all_details:
            students_service.output_all_students_with_summary()
        elif selected_option == Options.output_youngest_and_oldest_details:
            students_service.output_details_of_youngest_and_oldest_students()
        elif selected_option == Options.add_new_student:
            students_service.add_new_student()
        elif selected_option == Options.search_for_student_by_id:
            students_service.search_by_id()
        elif selected_option == Options.exit:
            break


main()
