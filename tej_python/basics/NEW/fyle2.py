#! usr/bin/python

#open a file
fo=open("hk.txt","r")
str=fo.read(15)
print "read string is",str

#check current position
pos=fo.tell()
print "current position",pos

#reposition pointer
beg=fo.seek(0,1)
str=fo.read(2)
print "after repositioning",str

#check current position
pos=fo.tell()
print "current position",pos
