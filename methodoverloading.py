#no method overloading in python



class Human:
 
    def sayHello(self, name=None):
 
        if name is not None:
            print 'Hello ' + name
        else:
            print 'Hello '
 
# Create instance
obj = Human()
 
# Call the method
print obj.sayHello()
 
# Call the method with a parameter
print obj.sayHello('Guido')
