from pythonds.basic.stack import Stack


    

def revstr(str):
    stack=Stack()

    for ch in str:
        stack.push(ch)
    r=''

    while not stack.isEmpty():
        r=r+stack.pop()

    return r

print revstr('abc')        
        
    
