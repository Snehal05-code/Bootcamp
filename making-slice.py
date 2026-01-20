

def main() :
	a = make([]int, 5)
	printSlice("a", a)

	b = make([]int, 0, 5)
	printSlice("b", b)

	c = b[:2]
	printSlice("c", c)

	d = c[2:5]
	printSlice("d", d)


def printSlice(s string, x []int):
	print("%s len=%d cap=%d %v\n",s, len(x), cap(x), x)
