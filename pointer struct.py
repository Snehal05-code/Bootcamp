class Vertex:
	def __init__(self, x, y):
		self.X = x
		self.Y = y



def main():
	v = Vertex(1, 2)
	p = v
	p.X = 1e9
	print(v)
	print(p)
	
	