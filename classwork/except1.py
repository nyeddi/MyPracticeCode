def print_nos():
    for i in range(10):
        a = 1
        print "caluculating"
        print i/a
        raise "NewException1"
        print " executing"
        print "1"
  
try:
    print_nos()

except ZeroDivisionError:
    print 'We got Zero division exception'
except NameError:
    print 'We dont know exception type--- wwe changed to nameerror'
except :
    print "anytype"
else:
    print 'this will executed when we dont have any excep in try block'
finally:
    print "always executed"
