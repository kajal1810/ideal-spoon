class Dog:

    kind="husky"

    def __init__(self,name):
        self.name=name

a=Dog("tom")
b=Dog("tommy")

print a.kind
print b.kind
print Dog.kind
print a.name
print b.name
