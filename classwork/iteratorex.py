class seq1:
   def __init__(self):
      self.x = 0

   def next(self):
      if self.x > 3:
         raise StopIteration
      self.x += 1
      return self.x**self.x

   def __iter__(self):
      return self

if __name__ == '__main__':
    s = seq1()
    #n = 0
    #for i in s:
    #   print i
    print s.next()
    print s.next()
    print s.next()
    print s.next()
    print s.next()
