import inspect


class Creator:

    """
        object_name -> reference to object which will be treated as chromosome
    """
    def __init__(self, object_reference):
        if inspect.isclass(object_reference):
            self.chromosome = object_reference
        else:
            raise TypeError('Value should be a reference to a class')

    """
        n -> amount of elements to be created
        args, kwargs -> arguments to initialize object
        return -> list of objects created using arguments
    """
    def create(self, n, *args, **kwargs):
        # print(n, end=" ")
        # print(*args, end=" ")
        # for key, val in kwargs.items():
        #     print("{} {}".format(key, val), end=" ")
        # print()
        return [self.chromosome(*args, **kwargs) for _ in range(0, n)]
