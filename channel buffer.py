from queue import Queue
ch = Queue(maxsize=2)

ch.put(1)
ch.put(2)

print(ch.get())
print(ch.get())
