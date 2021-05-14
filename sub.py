from multiprocessing import Process, Pipe
from random import randint
import os
from time import sleep

def f(conn):
    count = 5
    i = 1
    while count>0:
       print(os.getpid()) 
       print("count", count)
       inc = randint(0, 9)
       count += inc
       print("count +", inc, "=", count)
       dec = randint(0, 9)
       conn.send(dec)
       print(os.getpid(),"SEND", dec)
       sleep(2)
       #sleeeeeeeep
       dec = conn.recv()
       print(os.getpid(),"RECV", dec)
       count -= dec
       print(os.getpid(),count,"--------")
       sleep(2)
       if count<=0:
          print("LOOSER ~~~~~~~~~~", os.getpid())
