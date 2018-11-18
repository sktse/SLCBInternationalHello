import string


class InputParser(object):
    @staticmethod
    def parse(input_string):
        """
        Lowers, strips, and removes trailing punctuation
        :param input_string: The input string
        :return: The parsed string
        """
        trimmed_input = input_string.strip().lower()
        if trimmed_input and trimmed_input[-1] in string.punctuation:
            return trimmed_input[:-1].strip()

        return trimmed_input


class SemicolonSeparatedParser(object):
    @staticmethod
    def parse(semicolon_string):
        """
        Parses semicolon separated strings into an array
        :param semicolon_string: The semicolong separated string
        :return: An array with the strings with semicolon separated
        """
        values = []
        semicolon_string = semicolon_string.split(";")
        for raw_value in semicolon_string:
            value = raw_value.strip()
            if value:
                # The input is valid and is not empty.
                values.append(value)
        return values
