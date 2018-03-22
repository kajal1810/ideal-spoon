from pythonds.basic.stack import Stack


def checkstr(str):

    s=Stack()

    index=0

    balanced=True

    while index < len(str) and balanced:

        a=str[index]

        if a in "({[":
            s.push(a)

        else:

            if s.isEmpty():
                return False

            else:

                top=s.pop()

                if not matches(top,a):
                    balanced=False

        index=index+1


    if balanced and s.isEmpty():
         return True

    else:
         return False



def matches(o,c):
    opens="{(["
    closers="})]"

    return opens.index(o) == closers.index(c)

print checkstr('[{()}]')
