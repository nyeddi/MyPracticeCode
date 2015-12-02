ip='192.23.4.5'
class Fraction(object):
    ip = NONE
    def __init__(self,a,b):
        self.num = a
        self.den = b
    def show(self):
        print self.num,'/',self.den
    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    def __add__(self,ob2):
        num1 = self.num*ob2.den+self.den*ob2.num
        den1 = self.den * ob2.den
        return Fraction(num1,den1)
    def __div__(self,ob2):
        return Fraction(self.num*ob2.den,self.den*ob2.num)
    def __eq__(self,ob2):
        return (self.num == ob2.num) & (self.den == ob2.den)
        
"""
F1 = Fraction(4,5)
F1.show()
print F1
F2 = Fraction(4,5)
print F1,F2

print F1+F2
print F1.__add__(F2)

print F1/F2

print F1==F2

"""
