#WAP to check palindrome or Palindrome checker

from pythonds.basic.deque import Deque #import Deque from pyhtonds 


def palcheck(str):

    d=Deque()

    for ch in str:

        d.addRear(ch)


    equal=True

    while d.size()>1 and equal:

        first=d.removeFront()
        last=d.removeRear()

        if first!=last:
            equal=False

    return equal



print palcheck("radar")
print palcheck("abc")
