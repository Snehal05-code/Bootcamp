import threading
from queue import Queue, Empty
import time

def fibonacci(c, quit):
    x, y = 0, 1
    while True:
        try:
            # Check if quit signal came
            if not quit.empty():
                print("quit")
                return

            # Send next fibonacci number
            c.put(x)
            x, y = y, x + y

            time.sleep(0.01)   # small delay to simulate select switching

        except Exception:
            pass


def main():
    c = Queue()
    quit = Queue()

    # Goroutine equivalent
    def receiver():
        for _ in range(10):
            print(c.get())
        quit.put(0)      # send quit signal

    t = threading.Thread(target=receiver)
    t.start()

    fibonacci(c, quit)

    t.join()


if __name__ == "__main__":
    main()
