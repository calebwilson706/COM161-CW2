from simple_term_menu import TerminalMenu


def select_option_from_list(options, title: str):
    menu = TerminalMenu(
        options,
        title=title
    )

    return options[
        menu.show()
    ]
