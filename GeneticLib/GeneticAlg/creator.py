import inspect


def create(object_name):
    print()
    if not inspect.isclass(object_name):
        raise TypeError('Value should be a reference to a class')
    else:
        object = object_name()
