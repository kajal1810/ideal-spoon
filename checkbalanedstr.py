#check string contains paraenthesis are balanced or not 

from pythonds.basic.stack import Stack


def checkstr(str):

    s=Stack()
    index=0
    balanced=True

    while index < len(str) and balanced:

        a=str[index]

        if a == "(":
            s.push(a)
                
        else:

            if s.isEmpty():
                balanced=False

            else:
                 s.pop()

        index=index+1

    if balanced and s.isEmpty():
             return True

    else:
             return False


print checkstr('()')
                 
print checkstr('(')
