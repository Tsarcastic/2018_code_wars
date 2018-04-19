"""https://www.codewars.com/kata/597770e98b4b340e5b000071/train/python ."""

class FileNameExtractor:
    def extract_file_name(self, dirty_file_name):
        date_tracker = False
        extension_tracker = False

        date_counter = 0

        while date_tracker is False:
            if dirty_file_name[date_counter] == "_":
                dirty_file_name = dirty_file_name[date_counter + 1:]
                date_tracker = True
            else:
                date_counter += 1

        while extension_tracker is False:
            current_letter = dirty_file_name[-1]
            dirty_file_name = dirty_file_name[:-1]
            if current_letter == ".":
                extension_tracker = True

        return dirty_file_name

"""
Ideal solution

class FileNameExtractor:
    def extract_file_name(name):
    # The file name we want is between the "_" and the second "." of the given string
        find_underline = name.find("_")
        find_1st_dot = name.find(".")
        find_2nd_dot = name.find(".", find_1st_dot + 1)

        return name[find_underline + 1: find_2nd_dot]

"""
