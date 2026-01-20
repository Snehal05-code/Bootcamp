
import datetime

def main():
    t= datetime.datetime.now()
    if t.hour < 12:
        print("Good morning!")
    elif t.hour < 17:
        print("Good afternoon.")
    else:
        print("Good evening.")
  
if __name__ == "__main__":
    main()
