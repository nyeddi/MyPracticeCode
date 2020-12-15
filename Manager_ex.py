from Employee_ex import Employee
class Manager(Employee, Exception):
    def __init__(self, name, age, salary, manpower):
        Employee.__init__(self, name, age, salary)
        self.__manpower = manpower

    def __str__(self):
        return Employee.__str__(self) + " manpower: " + str(self.__manpower)

    def print_employee(self, data1, data2="data"):
        Employee.print_employee(data1,data2)
        print(data1,data2)


if __name__ == '__main__':
    # e1 = Employee('deepak', 24)
    # print( Employee.__doc__)
    # e2 = Employee('deepakkumar', 25)
    # print( e2)
    # # print e2.GetEmpCount()
    # del e1
    # print e2.GetEmpCount()
    M1 = Manager('shankar', 45, 10000000, 13)
    print(M1)
    print('Manager has these methods', dir(Manager))
