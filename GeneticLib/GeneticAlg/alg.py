from GeneticAlg import creator


class A:
    def __init__(self, text, number, a):
        self.text = text
        self.number = number


def main():
    # a = A()
    crt = creator.Creator(A)
    chromosomes = crt.create(5, "world", a="t", number=5)
    # try:
    #     creator.create("a")
    #
    # except Exception as e:
    #     print(e.args)
    for chromosome in chromosomes:
        print(chromosome.text, end=" ")


if __name__ == "__main__":
    main()
