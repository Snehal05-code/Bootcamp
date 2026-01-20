# struct Vertex → class Vertex
class Vertex:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # func (v *Vertex) Scale(f)
    def Scale(self, f):
        self.X = self.X * f
        self.Y = self.Y * f


# func ScaleFunc(v *Vertex, f)
def ScaleFunc(v, f):
    v.X = v.X * f
    v.Y = v.Y * f


def main():
    v = Vertex(3, 4)

    # v.Scale(2)
    v.Scale(2)

    # ScaleFunc(&v, 10)
    ScaleFunc(v, 10)

    p = Vertex(4, 3)

    # p.Scale(3)
    p.Scale(3)

    # ScaleFunc(p, 8)
    ScaleFunc(p, 8)

    print(v.__dict__, p.__dict__)


if __name__ == "__main__":
    main()
