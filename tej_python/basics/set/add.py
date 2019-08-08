a={1,2,3,4}
a.add(8)
print a
a.remove(4)
print a

b=2 not in a

print b
#a.clear()
#print a
b={9,8,7,6,2,4}
c=a & b
print c

c=a - b
print c

c=a^b
print c
print "****************** union"
print a.union(b)
