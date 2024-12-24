from multiprocessing import Queue
custom=Queue(maxsize=3)
custom.put(1)
print(custom.qsize())