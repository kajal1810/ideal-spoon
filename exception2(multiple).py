#multiple exceptions

try:  
    a=10/0;
    
except ArithmeticError,ValueError:  
    print "Arithmetic Exception"  

else:  
    print "Successfully Done"  
