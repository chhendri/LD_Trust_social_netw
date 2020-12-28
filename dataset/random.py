import random
import string

class Random_input(object):
    """Class for making a random input of tuples (sender, receiver, time) of size N, l is the size of the strings used as names,
        default is l=2"""

    def __init__(self, n, l=2):
        # Length of the names
        self.ls = l
        # Number of tuples to make
        self.N = n
        # Letters of the alphabet
        self.LETTERS = string.ascii_lowercase
        # Beginning and end time
        self.T_min = 0; self.T_max = 1000

    def __random_string(self, length):
        """Random string generator of given length"""
        return ''.join(random.choice(self.LETTERS) for i in range(length))

    def __random_time(self):
        """Random time generator"""
        return random.randint(self.T_min, self.T_max)

    def input_generator(self):
        """Generator of random set of tuples (sender, receiver, time) with given number of occurences N"""
        res = set()
        i = 0
        while i < self.N:
            sender = self.__random_string(self.ls)
            receiver = self.__random_string(self.ls)
            # Cannot send a message to itself
            if sender != receiver:
                res.add((sender, receiver, self.__random_time()))
            i += 1
        return res

