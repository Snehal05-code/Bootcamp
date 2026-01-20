
class Vertex:
	def __init__(self, x, y):
		self.X = x
		self.Y = y


var (
	v1 = Vertex(1, 2)  // has type Vertex
	v2 = Vertex(X=1)   // Y:0 is implicit
	v3 = Vertex()      // X:0 and Y:0
	p  = &v1
	
)

def main():
	print(v1, p, v2, v3)
