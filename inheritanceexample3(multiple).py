#multiple example

class Animal:   #base class 1
 
    def eat(self):  
      print 'Eating...This is base class1'  

class Dog:  #base class 2  

   def bark(self):
       print 'Barking... This is base class 2'  

class BabyDog(Animal,Dog):  #derived class 1 
    def weep(self):  
        print 'Weeping...This is derived class 1'  

d=BabyDog() #create obj of derived class 1 and this obj can access methods of all 3 clasees  

d.eat()  
d.bark()  
d.weep()  
