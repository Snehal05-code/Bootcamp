import math

# struct Vertex
class Vertex:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


# func Abs(v Vertex)
def Abs(v):
    return math.sqrt(v.X * v.X + v.Y * v.Y)


# func Scale(v *Vertex, f float64)
def Scale(v, f):
    v.X = v.X * f
    v.Y = v.Y * f


def main():
    v = Vertex(3, 4)

    # Scale(&v, 10) → Scale(v, 10)
    Scale(v, 10)

    print(Abs(v))


if __name__ == "__main__":
    main()
