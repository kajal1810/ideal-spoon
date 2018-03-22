#user define exception


class Notequalnos(Exception): #derive from Exception class

    pass

n1=input("enter no1: ")
n2=input("enter no2: ")

try:

    if n1!=n2:
        raise Notequalnos

    else:
        print "equal no"

except Notequalnos:
    print "nos are not equal"
        
