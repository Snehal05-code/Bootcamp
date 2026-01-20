import math

# struct Vertex → class Vertex
class Vertex:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


# normal function Abs(v Vertex)
def Abs(v):
    return math.sqrt(v.X * v.X + v.Y * v.Y)


def main():
    v = Vertex(3, 4)
    print(Abs(v))


if __name__ == "__main__":
    main()
