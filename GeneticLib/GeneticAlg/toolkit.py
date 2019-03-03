class Toolkit:

    def __init__(self):
        self.weights = tuple()

    """
        setting fitness weights -> 
            <0 -> minimize
            >0 -> maximize
    """

    def set_fitness_weights(self, weights):
        if type(weights) is tuple:
            for element in weights:
                if type(element) is not float:
                    raise TypeError('All weights must be floats!')

            self.weights = weights
        else:
            raise TypeError('Weights must be passed in tuple!')

    """
        list of objects is converted to list of 'individuals'
        return -> [(object, fitval_1, fitval_2, ...), ...]
    """

    @staticmethod
    def create_individuals(chromosomes):
        if type(chromosomes) is list:
            return [Individual(chromosome) for chromosome in chromosomes]
        else:
            raise TypeError('Chromosomes should be passed in list!')

    """
        input:
            individuals, list of attributes which will be used by functions specified in list of functions
        modifying existing population, not creating new one  
    """

    def calculate_fitness_values(self, individuals, list_of_attributes, list_of_funcs):
        if type(individuals) is not list:
            raise TypeError('Individuals should be stored in a list!')
        if type(list_of_funcs) is not list:
            raise TypeError('Fitness functions should be stored in a list!')
        if type(list_of_attributes) is not list:
            raise TypeError('Attributes should be stored in list!')
        if len(list_of_funcs) != len(self.weights):
            raise ValueError('Amount of functions should be equal amount of weights!')

        if len(list_of_attributes) < len(self.weights):
            list_of_attributes += [list_of_attributes[-1] for _ in range(0, len(self.weights) - len(list_of_attributes))]

        for individual in individuals:
            individual.values = tuple(func(getattr(individual.chromosome, attribute)) for func, attribute in
                                      zip(list_of_funcs, list_of_attributes))


class Individual:

    def __init__(self, chromosome=None):
        self.chromosome = chromosome
        self.values = None
