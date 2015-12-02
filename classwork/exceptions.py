from UsrdefinedExcep import InputError
try:
   #fh = open("testfile", "r")
   #fh.write("This is my test file for exception handling!!")
   Dbfailed = True
   if Dbfailed:
    raise InputError('mydatabase',' db is unavialbale exception raised')
   print 10
except InputError, e:
   print "Error: User defined exception ",e.expr," ",e.msg
else:
   print "Written content in the file successfully"
   #fh.close()
finally:
   print "Error: can\'t find file or read data"
