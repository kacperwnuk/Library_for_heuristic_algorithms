import unittest
from GeneticAlg import toolkit


class Test:
    @staticmethod
    def func(value):
        return value * 2


class TestToolkitMethods(unittest.TestCase):

    def setUp(self):
        self.toolkit = toolkit.Toolkit()
        self.individuals = [toolkit.Individual(1), toolkit.Individual(2)]

    def test_set_fitness_weights_when_wrong_values(self):
        weights = ("1", 2, 3)
        with self.assertRaises(TypeError):
            self.toolkit.set_fitness_weights(weights)

    def test_set_fitness_weights_when_correct_values(self):
        weights = (1.0, 2.0, 3.0)
        self.toolkit.set_fitness_weights(weights)
        self.assertEqual(weights, self.toolkit.weights)

    def test_creating_individuals(self):
        chromosomes = [1, 2, 3, 4]
        indvs = self.toolkit.create_individuals(chromosomes)
        self.assertEqual(len(indvs), len(chromosomes))

    def test_creating_individuals_with_wrong_chromosomes(self):
        chromosomes = (1, 2, 3, 4)
        with self.assertRaises(TypeError):
            self.toolkit.create_individuals(chromosomes)

    def test_calculating_fitness_values_with_bad_stored_individuals(self):
        indvs = (toolkit.Individual(1), toolkit.Individual(2))
        with self.assertRaises(TypeError):
            self.toolkit.calculate_fitness_values(indvs, ["attributes"], [Test.func])

    def test_calculating_fitness_values_with_bad_stored_attributes(self):
        with self.assertRaises(TypeError):
            self.toolkit.calculate_fitness_values(self.individuals, ("atttribute1", "attribute2"), [Test.func])

    def test_calculating_fitness_values_with_bad_stored_functions(self):
        with self.assertRaises(TypeError):
            self.toolkit.calculate_fitness_values(self.individuals, ["atttribute1", "attribute2"], (Test.func, ))
