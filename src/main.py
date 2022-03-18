from src.services.StudentsService import StudentsService
from src.utils.inputs.SelectOptionFromList import select_option_from_list


class Options:
    output_all_details = "Output all students details and a summary"
    output_youngest_and_oldest_details = "Output the details of the youngest and oldest student"
    add_new_student = "Add a new student to the file"
    search_for_student_by_id = "Search for a student by their student number"
    output_sorted_students = "Output the list of students sorted"
    show_bar_chart = "Show a bar chart of the amount of students from each country"
    exit = "Exit the program"


def main():
    options = [
        Options.output_all_details,
        Options.output_youngest_and_oldest_details,
        Options.add_new_student,
        Options.search_for_student_by_id,
        Options.output_sorted_students,
        Options.show_bar_chart,
        Options.exit
    ]

    students_service = StudentsService("data/students.txt")

    while True:
        selected_option = select_option_from_list(
            options,
            "Select what you would like to do:"
        )

        print("You have selected:", selected_option, "\n")

        if selected_option == Options.output_all_details:
            students_service.output_all_students_with_summary()
        elif selected_option == Options.output_youngest_and_oldest_details:
            students_service.output_details_of_youngest_and_oldest_students()
        elif selected_option == Options.add_new_student:
            students_service.add_new_student()
        elif selected_option == Options.search_for_student_by_id:
            students_service.search_by_id()
        elif selected_option == Options.output_sorted_students:
            selected_field = select_option_from_list(
                ["age", "surname"],
                "Select what you would like to sort by:"
            )
            students_service.output_sorted_students(selected_field)
        elif selected_option == Options.show_bar_chart:
            students_service.show_countries_bar_chart()
        elif selected_option == Options.exit:
            break


main()
