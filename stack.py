#from pythonds.basic.stack import Stack #import stack


class abc: #create class
     def __init__(self): #initialize items to an empty list
         self.items = []

     def isEmpty(self): #checks if list is empty or not 
         return self.items == []

     def push(self, item): #add item to items list
         self.items.append(item)

     def pop(self):  #delete item from list
         return self.items.pop()

     def peek(self): #return last pushed item 
         return self.items[len(self.items)-1]

     def size(self): #return size of stack
         return len(self.items)


s=abc()
print s.isEmpty()
s.push(4)
s.push(56)
print s.peek()
s.push("devanshi")
print s.size()
print s.pop()
print s.size()
print s.isEmpty()

