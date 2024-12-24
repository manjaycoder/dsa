import queue as q
custom=q.Queue(maxsize=3)
custom.put(1)
print(custom.qsize())