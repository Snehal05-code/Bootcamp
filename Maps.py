class Vertex:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __str__(self):
        return f"({self.lat}, {self.long})"


def main():
    
    m = {}

    
    m["Bell Labs"] = Vertex(40.68433, -74.39967)

    print(m["Bell Labs"])


main()
