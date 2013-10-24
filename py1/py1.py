__author__ = 'luoguoling'
class PrintIn(object):
    def __init__(self,name,age):
        self.name = 'rolling'
        self.age = 20
    def PrintIn(self):
        self.name = 'abc'
        print "his name is %s" % self.name

A = PrintIn("3aa",20)
print A.name
print A.age
print A.PrintIn()

