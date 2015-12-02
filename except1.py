from  UsrdefinedExcep import InputError
def print_nos():
    for i in range(1):
        a = 1
        print "caluculating"
        print i/a
        raise InputError("i/a","some Error")
        print " executing"
        print "1"
  
try:
    print_nos()
except InputError as a :
    print a.expr,a.msg
else:
    print 'this will executed when we dont have any excep in try block'
finally:
    print "always executed"
