class Stack:
    def __init__(self):
       self.lst = []
    
    def isEmpty(self):
        return self.lst == []
        
    def push(self,elm):
        self.lst.append(elm)
    
    def pop(self):
        return self.lst.pop()
    
    def peek(self):
        return self.lst[len(self.lst)-1]
    
    def size(self):
        return len(self.lst)
        
s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
print(s.pop())
        
      