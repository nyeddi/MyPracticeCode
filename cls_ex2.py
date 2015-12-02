class Test(object):
    pass
class Test1(Test):
    pass

class Employee(Test1):
   '''Common base class for all employees'''
   companyname = "xyz"
   __empCount = 0
   
   def __init__(self, name, salary,AGE):
      '''Initializing the class Employee''' 
      self.name = name
      self.salary = salary
      self.age = AGE
      #self.eno = eno
      Employee.__empCount += 1
   
   def displayCount(self):
     ''' Total employees '''
     print "Total Employee %d" % Employee.__empCount

   def displayEmployee(self):
      print "Name : ", self.name, "Age : ",self.age, ", Salary: ", self.salary, ", company: ",Employee.companyname
   def __del__(self):
       print "Destroy the current class"
       Employee.__empCount -= 1

if __name__ == "__main__":
   emp1 = Employee("raj",30000,26)
   #emp1.displayCount()
   emp1.displayEmployee()

   emp2 = Employee("ravi",40000,27)
   emp2.displayEmployee()

   emp1.eno =1001
   print emp1.eno
   print Employee.__doc__
   emp2.displayCount()
   print Employee.displayCount.__doc__

   print "emp count", Employee._Employee__empCount

   #print "Employee.__doc__:", Employee.__doc__
   #print "Employee.__name__:", Employee.__name__
   #print "Employee.__module__:", Employee.__module__
   print "Employee.__bases__:", Employee.__bases__
   #print "Employee.__dict__:", Employee.__dict__

   del emp1
   Employee.__del__(emp2)
   emp2.displayCount()
