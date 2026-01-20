import threading
from queue import Queue

def sum_list(s, c):
    total = 0
    for v in s:
        total += v
    c.put(total)     


def main():
    s = [7, 2, 8, -9, 4, 0]

    c = Queue()      

    
    t1 = threading.Thread(target=sum_list, args=(s[:len(s)//2], c))
    t2 = threading.Thread(target=sum_list, args=(s[len(s)//2:], c))

    t1.start()
    t2.start()

    x = c.get()
    y = c.get()

    t1.join()
    t2.join()

    print(x, y, x + y)


main()
