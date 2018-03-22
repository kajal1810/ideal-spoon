#multi level example

class Animal:   #base class

    def eat(self):  
      print 'Eating...This is base class'  

class Dog(Animal):  #derived class 1  

   def bark(self):
       print 'Barking... This is derived class 1'  

class BabyDog(Dog):  #derived class 2  
    def weep(self):  
        print 'Weeping...This is derived class 2'  

d=BabyDog() #create obj of derived class 2 and this obj can access methods of all 3 clasees  

d.eat()  
d.bark()  
d.weep()  
