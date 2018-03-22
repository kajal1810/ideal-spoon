from pythonds.basic.stack import Stack  #import Stack from pyhtonds


    

def revstr(str): #create method for reverse string 

    stack=Stack() #create obj of Stack

    r='' #take empty string
     
    for ch in str: #for every character in string which is passed in function
        stack.push(ch)#push every character od that string into stack

   

    while not stack.isEmpty(): #while stck is not empty pop every character from stack
        r=r+stack.pop() #store every poped charater into empty string r

    return r 

print revstr('abc')        
print revstr('devanshi')        
    
