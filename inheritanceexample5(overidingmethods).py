class Baseclass:        # define parent class
   def myMethod(self):
      print 'Calling base class method'

class Derivedclass(Baseclass): # define child class
   def myMethod(self):
      print 'Calling child method'

c = Derivedclass()          # instance of child
c.myMethod()         # child calls overridden method
