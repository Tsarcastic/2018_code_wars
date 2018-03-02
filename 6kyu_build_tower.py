def tower_builder(n_floors):
    the_list = []
    this_row = ""
    middle_of_row = "*"
    counter = n_floors - 1

    def empty_spaces():
        spaces = ""
        for n in counter:
            spaces += " "
        return spaces

    this_row += empty_spaces()
    this_row += middle_of_row
    this_row += empty_spaces()
    the_list.append(this_row)
    this_row = ""
    counter -= 1

    for n in counter:
        empty_spaces
    middle_of_row += "**"
    this_row += middle_of_row


