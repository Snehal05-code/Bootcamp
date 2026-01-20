def main(): 
	s = [2, 3, 5, 7, 11, 13]
	printSlice(s)

	s = s[:0]
	printSlice(s)

	s = s[:4]
	printSlice(s)

	
	s = s[2:]
	printSlice(s)

def printSlice(s):
	print("len=%d %v" % (len(s), s))
if __name__ == "__main__":
	        main()