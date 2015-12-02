class Parent(object):
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      Parent.__init__(self)
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'
      
   def parentMethod(self):
      print 'Calling child method'
      
   def __del__(self):
       print "calling __del in child"

c1 = Child()
c1.parentMethod()
del c1
