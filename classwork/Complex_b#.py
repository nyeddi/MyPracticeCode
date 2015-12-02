class complex(object):
     def __init__(self,x,y):
         self.__x = x
         self.__y = y
     def __str__(self):
         if x>10:
             print 'something'
             if y>10:
                 
         return "My complex No is: {}+i{}".format(self.__x,self.__y)
     def __add__(self,obj2):
         return complex(self.__x+obj2.__x,self.__y+obj2.__y)
     def __sub__(self,obj2):
         return complex(self.__x-obj2.__x,self.__y-obj2.__y)
     def __mul__(self,obj2):
         return complex(self.__x*obj2.__x,self.__y*obj2.__y)

     


c1 = complex(10,20)
c2 = complex(20,30)
print c1
print c1+c2,c1.__add__(c2),complex.__add__(c1,c2)
print c1-c2
print c1*c2

         


    
