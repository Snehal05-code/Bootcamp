import math

class Vertex:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    
    def Abs(self):
        return math.sqrt(self.X * self.X + self.Y * self.Y)


def main():
    v = Vertex(3, 4)
    print(v.Abs())


if __name__ == "__main__":
    main()
