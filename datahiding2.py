class car:
    __speed=0   #private datamemeber

    def __init__(self):

        self.__speed=200 #private data member cant access outside the class
                         #it should be access through within class with the help of methods of class

    def drive(self):
            print "speed is ", self.__speed

    def setspeed(self,speed):

            self.__speed=speed   #can set value with the help of methods of class 


r=car()
r.drive()
r.setspeed(40)
r.drive()

print r.__speed #error because data memeber is private cant access by obj directly

