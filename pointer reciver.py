import math

class Vertex:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # func (v Vertex) Abs()
    def Abs(self):
        return math.sqrt(self.X * self.X + self.Y * self.Y)

    # func (v *Vertex) Scale(f float64)
    def Scale(self, f):
        self.X = self.X * f
        self.Y = self.Y * f


def main():
    v = Vertex(3, 4)
    v.Scale(10)        # modifies the object (like pointer receiver)
    print(v.Abs())


if __name__ == "__main__":
    main()

