

class Vertex:
	def __init__(self, x, y):
		self.X = x
		self.Y = y


def main(): 
	v = Vertex(1, 2)
	v.X = 4
	print(v.X)
if __name__ == "__main__":
	main()