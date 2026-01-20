import math

# type MyFloat float64  → class MyFloat
class MyFloat:
    def __init__(self, value):
        self.value = float(value)

    # method Abs()
    def Abs(self):
        if self.value < 0:
            return -self.value
        return self.value


def main():
    f = MyFloat(-math.sqrt(2))
    print(f.Abs())


if __name__ == "__main__":
    main()
