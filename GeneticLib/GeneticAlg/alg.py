from GeneticAlg import creator
from GeneticAlg import toolkit
import random


class A:
    def __init__(self, text, number, a):
        self.text = text
        self.number = random.randint(0, number)


class Chromosome:
    def __init__(self, n):
        self.binary = [random.randint(0, 1) for _ in range(0, n)]


def fitness(chromosome):
    return chromosome.count(1)


def fit2(chromosome):
    return chromosome.count(0)


def main():
    # a = A()
    crt = creator.Creator(Chromosome)
    chromosomes = crt.create(5, 5)
    tools = toolkit.Toolkit()
    tools.set_fitness_weights(weights=(-1.0, 1.0))
    population = tools.create_individuals(chromosomes)
    tools.calculate_fitness_values(population, ["binary"], [fitness, fit2])
    pop = population
    population = tools.select_roulette(population, 4, key=0)
    # try:
    #     creator.create("a")
    #
    # except Exception as e:
    #     print(e.args)
    # for chromosome in chromosomes:
    #     print(chromosome.number, end=" ")
    for individual in pop:
        print("{} -> {}".format(individual.chromosome.binary, individual.values))
    print()
    for individual in population:
        print("{} -> {}".format(individual.chromosome.binary, individual.values))


if __name__ == "__main__":
    main()
