import random


class Toolkit:

    def __init__(self):
        self.weights = tuple()

    def set_fitness_weights(self, weights):
        """
            Setting fitness weights:
                <0 -> minimize
                >=0 -> maximize

            Attributes:
                weights: tuple of floats
        """

        if type(weights) is tuple:
            for element in weights:
                if type(element) is not float:
                    raise TypeError('All weights must be floats!')

            self.weights = weights
        else:
            raise TypeError('Weights must be passed in tuple!')

    @staticmethod
    def create_individuals(chromosomes):
        """
            List of objects is converted to list of 'individuals'
            Attributes:
                chromosomes: list of objects
            Returns:
                list of individuals
                [(object, fitval_1, fitval_2, ...), ...]
            Raises:
                TypeError if chromosomes are not stored in list
        """

        if type(chromosomes) is list:
            return [Individual(chromosome) for chromosome in chromosomes]
        else:
            raise TypeError('Chromosomes should be passed in list!')

    def calculate_fitness_values(self, individuals, list_of_attributes, list_of_funcs):
        """
            Modifying existing population, not creating new one
            Attributes:
                individuals: list of individuals
                list_of_attributes: list of attributes used to calculate fitness value
                list_of_funcs: list if functions used to calculate fitness value
            Raises:
                TypeError: when attributes are not stored in a list
                ValueError: when the amount of elements in list_of_funcs is not equal list of weights
        """

        if type(individuals) is not list:
            raise TypeError('Individuals should be stored in a list!')
        if type(list_of_funcs) is not list:
            raise TypeError('Fitness functions should be stored in a list!')
        if type(list_of_attributes) is not list:
            raise TypeError('Attributes should be stored in list!')
        if len(list_of_funcs) != len(self.weights):
            raise ValueError('Amount of functions should be equal amount of weights!')

        if len(list_of_attributes) < len(self.weights):
            list_of_attributes += [list_of_attributes[-1] for _ in
                                   range(0, len(self.weights) - len(list_of_attributes))]

        for individual in individuals:
            individual.values = tuple(func(getattr(individual.chromosome, attribute)) for func, attribute in
                                      zip(list_of_funcs, list_of_attributes))

    @staticmethod
    def select_random(individuals, k):
        """
            Attributes:
                individuals: list of individuals
                k: amount of individuals to be picked
            Returns:
                list of individuals
        """

        return random.sample(individuals, k)

    def select_best(self, individuals, k, key=0):
        """
            Picks best k individuals
            Attributes:
                individuals: list of individuals
                k: amount of individuals to be picked
                key: determines which fitness value should be used
            Locals:
                should_reverse: determines if function is minimizing or maximizing fitness value
            Returns:
                list of picked individuals
        """
        should_reverse = False
        if self.weights[key] >= 0:
            should_reverse = True

        return sorted(individuals, key=lambda x: x.values[key], reverse=should_reverse)[:k]

    def select_worst(self, individuals, k, key=0):
        """
            Picks worst k individuals
            Attributes:
                individuals: list of individuals
                k: amount of individuals to be picked
                key: determines which fitness value should be used
            Locals:
                should_reverse: determines if function is minimizing or maximizing fitness value
            Returns:
                list of picked individuals
        """
        should_reverse = False
        if self.weights[key] >= 0:
            should_reverse = True

        return sorted(individuals, key=lambda x: x.values[key], reverse=should_reverse)[:k]

    def select_roulette(self, individuals, k, key=0):
        """
            Picks k individuals using roulette method
            https://en.wikipedia.org/wiki/Fitness_proportionate_selection
            It is possible that in a return list there will be duplications of individuals!
            Attributes:
                individuals: list of individuals
                k: amount of individuals to be picked
                key: determines which fitness value should be used
            Locals:
                should_reverse: determines if function is minimizing or maximizing fitness value
            Returns:
                list of picked individuals
        """
        chosen = []

        if self.weights[key] >= 0:
            inds = sorted(individuals, key=lambda x: x.values[key], reverse=True)
            sum_values = sum(ind.values[key] for ind in inds)
            for _ in range(0, k):
                rand_choice = random.randrange(1, sum_values + 1)
                _sum = 0
                for ind in inds:
                    _sum += ind.values[key]
                    if _sum >= rand_choice:
                        chosen.append(ind)
                        print(_sum)
                        break
        else:
            inds = sorted(individuals, key=lambda x: x.values[key], reverse=False)
            """ values used in roulette f = fmax - f"""
            values = [inds[-1].values[key] - ind.values[key] for ind in inds]
            sum_values = sum(values)
            for _ in range(0, k):
                rand_choice = random.randrange(1, sum_values + 1)
                _sum = 0

                for i in range(0, len(inds)):
                    _sum += values[i]
                    if _sum >= rand_choice:
                        chosen.append(inds[i])
                        print(_sum)
                        break

        return chosen


class Individual:

    def __init__(self, chromosome=None):
        self.chromosome = chromosome
        self.values = None
