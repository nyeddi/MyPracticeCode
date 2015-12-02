def temp_convert(var):
   try:
      x = int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument
   else:
       print "No exception"
   finally:
       print "excuting the everytime"
temp_convert('xyz')
temp_convert(12.5)
