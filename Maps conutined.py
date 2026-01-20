class Vertex:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __repr__(self):
        return f"({self.lat}, {self.long})"


def main():
    # map[string]Vertex → Python dictionary
    m = {
        "Bell Labs": Vertex(40.68433, -74.39967),
        "Google": Vertex(37.42202, -122.08408)
    }

    print(m)

main()
