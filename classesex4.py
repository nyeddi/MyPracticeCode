class student(object):
    """ My class student"""
    __count = 0
    def __init__(self,name,age,rno,pno):
        self.__name = name
        self.__age = age
        self.__rno = rno
        self.phno = pno
        print "im in constructor"
        student.__count +=1
    def printStudent(self):
        print self.__name,self.__age,self.__rno,student.__count
    def GetStudentCount(self):
        return student.__count
    def __del__(self):
        student.__count -= 1
    def __str__(self):
        return "Student name is {} age {}".format(self.__name,self.__age)
        
s1 = student('naveen',26,12345,345)
print "dict",student.__bases__
print s1

print "count is :",s1.GetStudentCount()
print "My private acess",s1._student__count
#print s1.__name
#s1.__name = 'xyz'
#print s1.__name
#s1.printStudent()
s1.phno = 445438
print s1.phno
s1.a = 10
print s1.a
#print s1.b
s2 = student('vinay',23,5467,4567)
print "count is :",s2.GetStudentCount()
#print s2.name,s2.age,s2.rno
s2.printStudent()
#print s2.a
s3 = student('vinay kumar',24,54678,54444)
s3.printStudent()
print "count is :",s3.GetStudentCount()
del s3
#s3.printStudent()
print "count is :",s2.GetStudentCount()
