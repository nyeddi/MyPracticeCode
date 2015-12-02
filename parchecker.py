from Stack import *
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            print "symbol:::",symbol
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                tp = s.pop()
                print "top:::",tp
                if not matches(tp,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(opn,clse):
    opens = "([{"
    closers = ")]}"
    print "opn ",opn,"clse ",clse
    return opens.index(opn) == closers.index(clse)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
