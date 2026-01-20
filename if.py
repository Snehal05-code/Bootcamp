

import math

def sqrt(x):
	if x < 0:
		return sqrt(-x) + "i"

	return str(math.sqrt(x))


def main():
	print(sqrt(2), sqrt(-4))

main()