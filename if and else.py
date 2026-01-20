import math

def pow_func(x, n, lim):
    v = math.pow(x, n)

    if v < lim:
        return v
    else:
        print(f"{v} >= {lim}")

    return lim


def main():
    print(
        pow_func(3, 2, 10),
        pow_func(3, 3, 20)
    )

main()
