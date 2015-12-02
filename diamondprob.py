class BaseClass(object):
  num_base_calls = 0
  def __init__(self):
      print " BAse"
      super(BaseClass,self).__init__()
  def call_me(self):
    #super(self.__class__,self).call_me()
    print("Calling method on Base Class")
    self.num_base_calls += 1

class LeftSubclass(BaseClass):
  num_left_calls = 0
  def __init__(self):
      print " LeftSubclass"
      super(LeftSubclass,self).__init__()
  def call_me(self):
    super(LeftSubclass,self).call_me()
    print("Calling method on Left Subclass")
    self.num_left_calls += 1

class RightSubclass(BaseClass):
  num_right_calls = 0
  def __init__(self):
      print " RightSubclass"
      super(RightSubclass,self).__init__()
  def call_me(self):
    super(RightSubclass,self).call_me()
    print("Calling method on Right Subclass")
    self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
  num_sub_calls = 0
  def __init__(self):
      print " Subclass"
      super(Subclass,self).__init__()
  def call_me(self):
    super(Subclass,self).call_me()
    print("Calling method on Subclass")
    self.num_sub_calls += 1

class Base(object):
    def __init__(self):
        super(Base, self).__init__()
        print "Base created"
class ChildA(Base):
    def __init__(self):
        super(ChildA,self).__init__()

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()
class ChildC(ChildA,ChildB):
    def __init__(self):
        super(ChildC, self).__init__()

class A(object):
    def __init__(self, v, *args, **kwargs):
        print "A:init:v[{0}]".format(v)
        kwargs['v']=v
        super(A, self).__init__(*args, **kwargs)
        self.v = v


class MixInF(object):
    def __init__(self, *args, **kwargs):
        print "IObject:init"
    def f(self, y):
        print "IObject:y[{0}]".format(y)


class B(MixInF):
    def __init__(self, v, *args, **kwargs):
        print "B:init:v[{0}]".format(v)
        kwargs['v']=v
        super(B, self).__init__(*args, **kwargs)
        self.v = v
    def f(self, y):
        print "B:f:v[{0}]:y[{1}]".format(self.v, y)
        super(B, self).f(y)


class C(MixInF):
    def __init__(self, w, *args, **kwargs):
        print "C:init:w[{0}]".format(w)
        kwargs['w']=w
        super(C, self).__init__(*args, **kwargs)
        self.w = w
    def f(self, y):
        print "C:f:w[{0}]:y[{1}]".format(self.w, y)
        super(C, self).f(y)


class Q(C,B):
    def __init__(self, v, w):
        super(Q, self).__init__(v=v, w=w)
    def f(self, y):
        print "Q:f:y[{0}]".format(y)
        super(Q, self).f(y)
        
q1 = Q(10,20)
q1.f(10)
#c1 = ChildC()
s1 =  Subclass()
print Subclass.mro()
s1.call_me()
