def main():
	import cmath
	ToBe = False
	MaxInt = 1<<64 - 1
	z = cmath.sqrt(-5 + 12j)

	print(f"Type: {type(ToBe)} Value: {ToBe}")
	print(f"Type: {type(MaxInt)} Value: {MaxInt}")
	print(f"Type: {type(z)} Value: {z}")

if __name__ == "__main__":
	main()