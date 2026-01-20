import threading
import time

# SafeCounter equivalent
class SafeCounter:
    def __init__(self):
        self.v = {}
        self.lock = threading.Lock()

    # Inc method
    def Inc(self, key):
        with self.lock:          # same as mu.Lock() / mu.Unlock()
            self.v[key] = self.v.get(key, 0) + 1

    # Value method
    def Value(self, key):
        with self.lock:
            return self.v.get(key, 0)


def main():
    c = SafeCounter()

    # create 1000 threads (like 1000 goroutines)
    threads = []
    for i in range(1000):
        t = threading.Thread(target=c.Inc, args=("somekey",))
        t.start()
        threads.append(t)

    # same as time.Sleep(time.Second)
    time.sleep(1)

    print(c.Value("somekey"))


if __name__ == "__main__":
    main()
