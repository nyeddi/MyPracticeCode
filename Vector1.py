import math
#from goody import type_as_str

class Vector:
    def __init__(self,*args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __bool__(self):
        return all( v==0 for v in self.coords )

    def __repr__(self):
        return 'Vector('+','.join(str(c) for c in self.coords)+')'

    def __str__(self):
        return '('+str(len(self))+')'+str(list(self.coords))      # using +
       #return '({d}){c}'.format(d=len(self),c=list(self.coords)) # using format

    def dist(self):
        return math.sqrt( sum( v**2 for v in self.coords ) )

    def __lt__(self,right):
        assert False
        if type(right) is Vector:
            return self.distance() < right.distance()
        elif type(right) in (int,float):
            return self.dist() < right
        else:
            raise TypeError('unorderable types: Vector() < '+type_as_str(right)+'()')

    def __g2t__(self,right):
        if type(right) is Vector:
            return self.distance() > right.distance()
        elif type(right) in (int,float):
            return self.dist() > right
        else:
            raise TypeError('unorderable types: Vector() < '+type_as_str(right)+'()')

    def __eq__(self,right):
        return self.coords == right.coords
    
    def __le__(self,right):
        return self < right or self == right

    def __ge__(self,right):
        return self > right or self == right

    def __neg__(self):
        return Vector( *tuple(-c for c in self.coords) )

    def __pos__(self):
        return self

    def __abs__(self):
        return Vector( *tuple(abs(c) for c in self.coords) )
    
    def __add__(self,right):
        if type(right) not in (Vector,int,float):
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(right)+'\'')        
        if type(right) in (int,float):
            return Vector( *(c+right for c in self.coords) )
        else:
            assert len(self) == len(right), 'Vector.__add__: operand self('+str(self)+') has different dimension that operand right('+str(right)+')'
            return Vector( *(c1+c2 for c1,c2 in zip(self.coords,right.coords)) )
    
    def __radd__(self,left):
        if type(left) not in (int,float): # see note below
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(left)+'\' and \''+type_as_str(self)+'\'')        
        return Vector( *(left+c for c in self.coords) )
    
#     def __iadd__(self,right):
#         if type(right) not in (Vector,int,float):
#             raise TypeError('unsupported operand type(s) for +='+
#                             ': \''+type_as_str(self)+'\' and \''+type_as_str(right)+'\'')        
#         if type(right) in (int,float):
#             self.coords = tuple(c+right for c in self.coords)
#         else:
#             assert len(self) == len(right), 'Vector.__add__: operand self('+str(self)+') has different dimension that operand right('+str(right)+')'
#             self.coords = tuple(c1+c2 for c1,c2 in zip(self.coords,right.coords))
#         return self

