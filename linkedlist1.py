#create node class

class Node:

    def __init__(self,initdata): #double _ 
        self.data=initdata
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext






n=Node(50)
n.getData()
    
