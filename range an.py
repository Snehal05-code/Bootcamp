import threading
from queue import Queue

def fibonacci(n, q):
    x, y = 0, 1
    for _ in range(n):
        q.put(x)
        x, y = y, x + y
    q.put(None)  # Signal that we're done

def main():
    q = Queue(maxsize=10)
    
    # Start the Fibonacci function in a separate thread
    t = threading.Thread(target=fibonacci, args=(q.maxsize, q))
    t.start()
    
    while True:
        val = q.get()
        if val is None:  
            break
        print(val)

    t.join()
