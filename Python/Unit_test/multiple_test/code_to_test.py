
def add(a, b):
    return a+b


def subtract(a: int, b: int) -> int:
    return a-b


def divide(a: [int, float], b: [int, float]):
    if b == 0:
        raise ValueError
    else:
        return a/b

    