"""This module declares a Employee and Manager classes"""
class Employee:
    'This is employee base class'
    __empcount = 0

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        print('init Employee')
        Employee.__empcount += 1

    def __str__(self):
        return "Emp name {} and age is {} salary is {}".format(self.__name, self.__age, self.__salary)

    @classmethod
    def GetEmpCount(cls):
        return cls.__empcount

    @staticmethod
    def print_employee(data1, data2="data"):
        print(data1,data2)

    def __add__(self, other_obj):
        return Employee("","",self.__salary+other_obj.__salary)

    def __del__(self):
        Employee.__empcount -= 1

if __name__ == '__main__':

    e1 = Employee('deepak', 24, 10)
    dct = {"deepak":24, "naveen":23}
    # emp_list = []
    # for name ,age in dct.items():
    #     emp_list.append(Employee(name, age))

    print( __doc__)
    print(Employee.GetEmpCount())
    e2 = Employee('deepakkumar', 25, 20)
    e3 = Employee('rajesh', 25, 30)
    print(    dir(e2))
    #print(Employee.__empcount)
    # print e2.GetEmpCount()
    del e1
    print (e2.GetEmpCount())
    print(e1+e2+e3)
