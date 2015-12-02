class Employee:
    __empCount = 0
    def __init__(self,name,age,sal):
        self.__name = name
        self.__age  = age
        self.__sal = sal
        Employee.__empCount += 1
    def __str__(self):
        return "name = {}, age = {}, sal = {}".format(self.__name,self.__age,self.__sal)
    def get_Emp_Count(self):
        return Employee.__empCount
    def __del__(self):
        print "Im in destructor"
        Employee.__empCount -= 1

class Manager(Employee):
    def __init__(self,name,age,sal,ManagesCnt):
        Employee.__init__(self,name,age,sal)
        self.__Manages = ManagesCnt

    def __str__(self):
        return Employee.__str__(self) + " ManagesCnt = {}".format(self.__Manages)


e1 = Employee('Sandy',25,345345)
print e1.get_Emp_Count()
e2 = Employee('Randy',23,34312)
print e2.get_Emp_Count()
#del e1
#print e2.get_Emp_Count()
#print Employee.__empCount
#print e1.__name
m1 = Manager("RRRRRR",45,54345345345,2)
print m1.get_Emp_Count()
print m1
print e1
