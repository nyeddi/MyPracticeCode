class LogicGate(object):
    def __init__(self,lbl):
        self.label = lbl
        self.output = None
    def getlabel(self):
        return self.label
    def getoutput(self):
        self.output = self.performLogic()
        return self.output
class BinaryGate(LogicGate):
    def __init__(self,lbl):
        LogicGate.__init__(self,lbl)

        pinA = None
        pinB = None
    def getpina(self):
        return int(input('enter the no for the gate'))
    def getpinb(self):
        return int(input('enter the no for the gate'))
            
class UnaryGate(LogicGate):
    def __init__(self,lbl):
        LogicGate.__init__(self,lbl)
        pin = None
    def getpin(self):
        return int(input('enter the no for the gate'))

class AndGate(BinaryGate):
    def __init__(self,lbl):
        BinaryGate.__init__(self,lbl)
       
    def performLogic(self):
        if self.getpina() == 1 & self.getpinb() == 1:
            return 1
        else:
            return 0
        
        
A1= AndGate('A1')
print A1.getlabel()
#A1.getpina()
#A1.getpinb()
print  A1.getoutput()

    
