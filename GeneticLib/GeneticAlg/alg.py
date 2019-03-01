from GeneticAlg import creator


class A:
    def __init__(self):
        print("hello")


def main():
    # a = A()
    creator.create(A)
    try:
        creator.create("a")

    except Exception as e:
        print(e.args)


if __name__ == "__main__":
    main()
