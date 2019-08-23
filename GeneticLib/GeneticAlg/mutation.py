import numpy.random


class Mutation:

    def __init__(self, mutation_probability):
        self.MPB = mutation_probability

    def mutate(self, individuals: list, mutate_function):
        """
            Attributes:
                individuals: list of individuals
                mutate_function: function used in mutating
        """
        for individual in individuals:
            if numpy.random.randint(0, 101, 1) < self.MPB:
                mutate_function(individual)

