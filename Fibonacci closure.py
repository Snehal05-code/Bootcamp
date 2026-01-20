
def fibonacci():
    a, b = 0, 1

    def next_number():
        nonlocal a, b      
        a, b = b, a + b
        return a

    return next_number
f = fibonacci()

for i in range(10):
    print(f())

