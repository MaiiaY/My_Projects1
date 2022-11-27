import random


def build(a, b):

    print('The list:', b)
    print('The quantity of numbers:', a)


c = random.randint(1, 10)
d = [random.randint(10, 60) for x in range(c)]
build(c, d)
