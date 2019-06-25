num=int(input("enter no."))
msg=input("enter msg  ")
l=len(msg)
msg2=input("enter msg22  ")
s=len(msg2)
n=num//2
for i in range(n):
    print(" "*(n-i-1) + "* " * (i+1),end="")
    if(num%2==0):
        for j in range(2*(n-i-1)):
            print(" ",end="")
    else:
        for j in range (2*(n-i-1)+1):
            print(" ",end="")
    for j in range (i+1):
        print("* ",end="")
    print()
if num%2==0:
    if l%2==0:
        print("* "*((num-l)//2) + " ".join(msg) + " *"*((num-l)//2)) #even even
    else:
        print("* "*((num-l)//2) + " ".join(msg) + " *"*(((num-l)//2)+1))# even odd
else:
    if l%2==0:
        print("* "*((num-l)//2) + " ".join(msg) + " *"*(((num-l)//2)+1)) # odd even
    else:
        print("* "*((num-l)//2) + " ".join(msg) + " *"*(((num-l)//2)))# odd odd

if num%2==0:
    if s%2==0:
        print("* "*((num-s)//2) + " ".join(msg2) + " *"*((num-s)//2))
    else:
        print("* "*((num-s)//2) + " ".join(msg2) + " *"*(((num-s)//2)+1))
else:
    if s%2==0:
        print("* "*((num-s)//2) + " ".join(msg2) + " *"*(((num-s)//2)+1))
    else:
        print("* "*((num-s)//2) + " ".join(msg2) + " *"*(((num-s)//2)))        
    
for i in range(num,0,-1):
    print(" "*(num-i) + "* "*(i))
    
