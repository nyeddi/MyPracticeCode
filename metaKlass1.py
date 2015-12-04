# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Return a class object, with the list of its attribute turned 
    into uppercase.
  """

  # pick up any attribute that doesn't start with '__' and uppercase it
  uppercase_attr = {}
  for name, val in future_class_attr.items():
      if not name.startswith('__'):
          uppercase_attr[name.upper()] = val
      else:
          uppercase_attr[name] = val

  # let `type` do the class creation
  return type(future_class_name, future_class_parents, uppercase_attr)

#commenting because trying to use class based metaclass
#__metaclass__ = upper_attr # this will affect all classes in the module

#################
class UpperAttrMetaclass(type): 

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

__metaclass__ = UpperAttrMetaclass # this will affect all classes in the module
#################

class Foo(): # global __metaclass__ won't work with "object" though
  # but we can define __metaclass__ here instead to affect only this class
  # and this will work with "object" children
  #__metaclass__ = UpperAttrMetaclass
  bar = 'bip'

print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True

f = Foo()
print(f.BAR)
# Out: 'bip'
'''
Python Guru Tim Peters

The main use case for a metaclass is creating an API. A typical example of this is the Django ORM.

It allows you to define something like this:

class Person(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
But if you do this:

guy = Person(name='bob', age='35')
print(guy.age)
It won't return an IntegerField object. It will return an int, and can even take it directly from the database.

This is possible because models.Model defines __metaclass__ and it uses some magic that will turn the Person you just defined with simple statements into a complex hook to a database field.

Django makes something complex look simple by exposing a simple API and using metaclasses, recreating code from this API to do the real job behind the scenes.
'''
