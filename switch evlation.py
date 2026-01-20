

import datetime


def main():
	print("When's Saturday?")
	today = datetime.datetime.now().weekday()
	saturday = 5
	
	if today == saturday:
		print("Today.")
	elif today == saturday - 1:
		print("Tomorrow.")
	elif today == saturday - 2:
		print("In two days.")
	else:
		print("Too far away.")


if __name__ == "__main__":
	main()
	
