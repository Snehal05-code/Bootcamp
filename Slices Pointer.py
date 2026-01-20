

def main():
	names = ["John", "Paul", "George", "Ringo"]
	print(names)

	a = names[0:2]
	b = names[1:3]
	print(a, b)

	b[0] = "XXX"
	print(a, b)
	print(names)
if __name__ == "__main__":
	main()