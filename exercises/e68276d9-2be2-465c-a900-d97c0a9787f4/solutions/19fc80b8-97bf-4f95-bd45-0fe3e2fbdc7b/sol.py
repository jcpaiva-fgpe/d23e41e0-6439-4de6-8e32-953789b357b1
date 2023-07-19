def generate_table(data):
    def get_column_width(column_data):
        return max(len(str(item)) for item in column_data)

    if not data:
        return ""

    num_columns = len(data[0])
    
    column_widths = [get_column_width(column) for column in zip(*data)]
    table = "+-" + "-+-".join("-" * width for width in column_widths) + "-+\n"
    header_row = "| " + " | ".join(str(data[0][i]).ljust(column_widths[i]) for i in range(num_columns)) + " |\n"
    table += header_row
    table += "+-" + "-+-".join("-" * width for width in column_widths) + "-+\n"
    
    for row in data[1:]:
        row_data = "| " + " | ".join(str(row[i]).ljust(column_widths[i]) for i in range(min(num_columns, len(row)))) + " |"
        table += row_data + "\n"

    table += "+-" + "-+-".join("-" * width for width in column_widths) + "-+"
    return table

input_data = [["Rok", "Mistrz"], [1986, "Argentyna"], [1990, "Niemcy"], [1994, "Brazylia"],
              [1998, "Francja"], [2002, "Brazylia"], [2006, "Włochy"], [2010, "Hiszpania"],
              [2014, "Niemcy"], [2018, "Francja"], [2022, "Argentyna"]]

output_table = generate_table(input_data)
print(output_table)
