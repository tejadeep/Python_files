
f=open("foo2.txt","w")
f.write("come here my dear")
f=open("foo2.txt","r")
d=f.tell()
print d

pos=f.seek(0,0)
d=f.tell()
print "pois is",d
m=f.read(8)
print "str is",m
