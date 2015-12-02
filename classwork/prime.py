def prime(num):
  for n in range(2, num):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n//x
                break
        else:
               print n, 'is a prime number'
         

def add(a,b):
    return a+b    

if __name__ == '__main__':
     prime(30)



