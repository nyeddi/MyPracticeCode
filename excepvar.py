# Define a function here.
class myerror(Exception):
    def __init__(self,arg):
        self.level = arg
        
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument

def functionName( level ):
   if level < 1:
      raise myerror(level)
      # The code below to this would not be executed
      # if we raise the exception


if __name__ == '__main__':
    try:
        functionName(0)
    except myerror,l:
        print "invalid",l.level
        
