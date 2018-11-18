import random


class BetterRandom(object):
    @staticmethod
    def _log(message, logger=None):
        if logger:
            logger.log(message)

    @staticmethod
    def random(length, logger=None):
        random_array = [random.randint(0, length * length) % length for p in range(0, 20)]
        BetterRandom._log("Random type selection pool: {}".format(random_array), logger)
        random_index = random.choice(random_array)

        is_reverse_index = random.randint(0, 1)
        BetterRandom._log("Is random index reversed? {}".format(is_reverse_index), logger)
        if is_reverse_index:
            random_index = length - random_index - 1

        BetterRandom._log("Random index: {}".format(random_index), logger)
        return random_index


class GreetingPicker(object):
    def __init__(self, standard_greetings, custom_greetings, custom_enabled, custom_percentage, logger=None):
        self.standard_greetings = standard_greetings
        self.custom_greetings = custom_greetings
        self.custom_enabled = custom_enabled
        self.custom_percentage = custom_percentage
        self.logger = logger

    def _log(self, message):
        if self.logger:
            self.logger.log(message)

    def pick(self):
        """
        Picks a random greeting.
        It will take into account custom greetings if enabled.
        :return: A random greeting string.
        """
        greeting_set = self.standard_greetings if self.pick_greeting_type() else self.custom_greetings
        greeting = self.get_random_from_set(greeting_set)
        return greeting

    def pick_greeting_type(self):
        """
        CustomOutputPercentage is between 1 and 100
        if the roll is less than CustomOutputPercentage, then it is custom greeting.  Otherwise default greeting.
        Example:
            * CustomOutputPercentage == 1 percent, roll is 0 ==> Show custom greeting.
            * CustomOutputPercentage == 1 percent, roll is 1+ ==> Show default greeting.

        This means, show custom greeting is
        ```
        is_custom_greeting = randomIndex < CustomOutputPercentage
        ```

        Therefore, show the default greeting is
        ```
        is_default_greeting = not is_custom_greeting
        is_default_greeting = not randomIndex < CustomOutputPercentage
        is_default_greeting = randomIndex >= CustomOutputPercentage
        ```

        :return: True if the default greeting. False for custom greeting.
        """
        if not self.custom_enabled:
            # if custom output greetings is disabled, just exit out immediately with default greetings.
            return True

        if self.custom_percentage == 0:
            # if custom output greetings is set to 0%, just exit out immediately with default greetings.
            return True

        random_index = BetterRandom.random(100, self.logger)
        is_default_greeting = random_index >= self.custom_percentage
        self._log("Is greeting type default? {}".format(is_default_greeting))

        return is_default_greeting

    def get_random_from_set(self, values):
        """
        Randomly picks a value from a set of values
        :param values: The set of values
        :return: A single value from the set
        """

        random_index = BetterRandom.random(len(values), self.logger)
        value = values[random_index]
        return value
