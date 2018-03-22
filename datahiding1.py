class car:
    def __init__(self):
        print "init method"
        self._light()

    def drive(self):
        print("class method drive")
        self._light()
    def _light(self): #private method
        print "private method of class accessed by init and drive method "



r=car()
r.drive()

r.light() #error
