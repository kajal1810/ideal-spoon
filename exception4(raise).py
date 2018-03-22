#raise exception


try:  
    a='devanshi'  
    print a  
    raise NameError("its a name error")  
except NameError as e:  
        print "An exception occurred:  "  
        print e  



