from simple_term_menu import TerminalMenu
from src.services.StudentsService import StudentsService

option_output_all_details = "Output the all students details and a summary"
option_exit = "Exit the program"


def main():
    options = [
        option_output_all_details,
        option_exit
    ]
    students_service = StudentsService("../data/students.txt")

    while True:
        menu = TerminalMenu(options)

        selected_option = options[menu.show()]

        if selected_option == option_output_all_details:
            students_service.output_all_students_with_summary()
        elif selected_option == option_exit:
            break


main()
