#nested if


cisco=raw_input("enter cisco password: ")

if cisco=="cisco":
    print "your cisco pass is correct"
    print"you can procced further"

    telnet=raw_input("enter telnet password: ")

    if telnet=="telnet":
        print"your telnet pass is correct"
    else:
        print "your telnet pass is wrong"
else:
    print "your cisco pass is wrong"
    
