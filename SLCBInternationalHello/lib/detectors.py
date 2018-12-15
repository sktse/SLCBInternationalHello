class GreetingDetector(object):
    def __init__(self, standard_greetings, custom_greetings, custom_enabled):
        self.standard_greetings = standard_greetings
        self.custom_greetings = custom_greetings
        self.custom_enabled = custom_enabled

        self.greetings_lookup = self.build_lookup(self.standard_greetings)
        self.custom_greeting_lookup = self.build_lookup(self.custom_greetings)

    def build_lookup(self, greetings):
        greetings_lookup = {}

        for greeting in greetings:
            greeting_words = greeting.split()
            greeting_length = len(greeting_words)

            if greeting_length not in greetings_lookup:
                greetings_lookup[greeting_length] = []

            greetings_lookup[greeting_length].append(greeting)

        return greetings_lookup

    def is_greeting(self, data):
        # The function `GetParamCount()` apparently returns a string?
        # https://github.com/AnkhHeart/Streamlabs-Chatbot-Python-Boilerplate/wiki/Data-Object#function-8
        # Convert it into an integer
        parameter_count = int(data.GetParamCount())

        length_keys = self.greetings_lookup.keys()
        for length in length_keys:
            if length > parameter_count:
                # We have greetings with a word count larger than the number of input words
                continue

            words = []
            for i in range(0, length):
                words.append(data.GetParam(i))
            input_greeting = unicode(" ".join(words).lower())
            greetings = self.greetings_lookup[length]

            if input_greeting in greetings:
                return True

        return False
