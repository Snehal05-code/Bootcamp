import math


def compute(fn):
    return fn(3, 4)


hypot = lambda x, y: math.sqrt(x*x + y*y)

print(hypot(5, 12))

print(compute(hypot))
print(compute(math.pow))
