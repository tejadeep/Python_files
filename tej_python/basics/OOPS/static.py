class test:
    x=10
    def __init__(self):
        al=90
        print (id(al))
        self.y=20
    def sub(self):
        self.k=800
        print (self.k)
    def sub2(self):
        self.sub()
    @classmethod
    def sub3(tej):
	tej=1000
        print ("***********************",tej)

t1=test()
t2=test()
#t1.sub()
t1.sub2()
test.sub3()
t1.sub3()
print(t1.x,t1.y)
print(t2.x,t2.y)
del test.x
t1.x=90
t2.x=89
print(t1.x,t1.y)
print(t2.x,t2.y)
