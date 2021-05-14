from multiprocessing import Process, Pipe
from random import randint
import os
from time import sleep
import sub

conn1, conn2 = Pipe()
p1 = Process(target=sub.f, args=(conn1,))
p2 = Process(target=sub.f, args=(conn2,))
p1.start()
p2.start()
p1.join()
p2.join()
