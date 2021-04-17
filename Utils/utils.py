import operator


def add(tup1, tup2):
    return tuple(map(operator.add, tup1, tup2))


def subtract(tup1, tup2):
    return tuple(map(operator.sub, tup1, tup2))
