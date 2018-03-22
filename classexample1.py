class Student:  #classname

    count=0     #class variable whose value is shared among all class instances
                #it can be accessed by classname.variablename
    

    def __init__(self,name,dept):       #its a special method called class constructor or initialization method.
                                        #Python calls this method when you create a new instance of this class.
        self.name=name    #attributes of instance
        self.dept=dept    #attributes of instance
        Student.count+=1  

    def displaycount(self):     #other simple normal method to display count
                                #ou declare other class methods like normal functions with the exception that the first argument to each method is self.
                                #Python adds the self argument to the list for you;
                                #you do not need to include it when you call the methods.
        print "total students= ",Student.count

    def disstu(self):           #normal method to dispaly parameters
        print "name= ",self.name
        print "dept= ",self.dept


s1=Student("abc","it") #create and initialize object
s1.disstu()             #display values of parameters or acceessing values of parameters
       
s2=Student("xyz","mech")
s2.disstu()
s1.displaycount()#display values of count

print hasattr(s1, 'dept')    # Returns true if 'age' attribute exists
print getattr(s1, 'dept')    # Returns value of 'age' attribute


#print setattr(s2, 'dept', 'comp') # Set attribute 'age' at 8
#print delattr(s1, 'dept')    # Delete attribute 'age'
#last two method gives wrong output




