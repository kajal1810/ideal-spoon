#simple exception

try:  
    a=10/0  
    print a  

except ArithmeticError:  
        print "cant divide by zero"  

else:  
    print "Welcome" 
