import string


class InputParser(object):
    @staticmethod
    def parse(input_string):
        trimmed_input = input_string.strip().lower()
        if trimmed_input and trimmed_input[-1] in string.punctuation:
            return trimmed_input[:-1].strip()

        return trimmed_input
