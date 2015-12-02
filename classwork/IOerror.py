try:
   fp = file('client.py','r')
except IOError:
    print "file IOerror"
except NameError:
    print "Name error"
except:
    print "error"
else:
    print "No exception"
finally:
    print "always in"
