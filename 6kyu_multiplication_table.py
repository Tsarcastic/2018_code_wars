def multiplication_table(row, col):
    the_table = []
    row_iteration = 0

    for i in range(row):
        row_iteration += 1
        col_iteration = 0
        table_row = []

        for i in range(col):
            col_iteration += 1
            append_value = row_iteration * col_iteration
            table_row.append(append_value)

        the_table.append(table_row)

    return the_table