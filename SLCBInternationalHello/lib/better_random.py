import random


class BetterRandom(object):
    @staticmethod
    def random(length):
        random_array = [random.randint(0, length * length) % length for p in range(0, 20)]
        random_index = random.choice(random_array)

        is_reverse_index = random.randint(0, 1)
        if is_reverse_index:
            random_index = length - random_index - 1

        return random_index
