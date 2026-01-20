def adder():
    sum = 0

    def inner(x):
        nonlocal sum   
        sum += x
        return sum

    return inner


pos = adder()
neg = adder()

for i in range(10):
    print(pos(i), neg(-2 * i))
