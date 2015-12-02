# fibonacci.py
# 1 1 2 3 5 8 ...
import time
import sys

def fib():
   a, b = 0, 1
   while True:
      yield b
      a, b = b, a + b


iter1 = fib()

try:
   for i in iter1:
      print i,
      time.sleep(3)
      sys.stdout.flush()
except KeyboardInterrupt:
   print "Calculation stopped"
