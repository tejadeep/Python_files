#import os
fo=open("foo2.txt","w")
fo.write("hii ra babu how are you ?")

fo=open("foo2.txt","r")
str1=fo.read(10)
print "The string is ",str1

pos=fo.seek(0,1)
d=fo.tell()
print "pos is ",d

str1=fo.read(5)
print "new is ",str1
