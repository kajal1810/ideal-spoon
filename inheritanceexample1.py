class Animal:       #base class   

    def eat(self):  #method of base class  
      print 'Eating... This is base class'
      
class Dog(Animal):     #derived class is Dog and base class is Animal

   def bark(self):      #method of derived class
      print 'Barking... This is drived class'  



d=Dog()  #create obj of derived class Dog , here __init()__ is not used because se dont have initialize obj
d.eat()  #obj of drived class called method of base class       
d.bark() #obj of drived class called method of drived class  
