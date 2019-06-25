########-------- S ---------#########
for row in range (7):
    for col in range (5):
        if ((row==0 or row==3 or row==6) and (col >0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)) :
            print ("*",end="")
        else:
            print(end=" ")
    print()
#print(end=" ")    
########-------- I ----------########    
for row in range(7):
    for col in range(5):
        if ((row==0 or row ==6) and (col>=0 and col<5)) or (col==2 and (row>0 and row <7)):
            print("*",end="")
        else:
            print(end=" ")
    print()    
#######-------- N -----------#########    
for row in range(7):
    for col in range(7):
        if col==0 or col ==6 or ( row==col and (col>0 and col <6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
########------- D ----------#######
for row in range(7):
    for col in range(7):
        if ((row==0 or row==6 )and (col!=5 and col!=6)) or ((row==1 or row==5) and col==5) or (col==6 and (row>1 and row<5)) or (col==1 and (row>0 and row<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()

########------- H ----------#######
for row in range(7):
    for col in range(7):
        if (col==0 or col==6 and (row>=0 and row<7)) or (row==3 and(col>0 and col<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()    
########------- U ----------#######
for row in range(7):
    for col in range(7):
        if ((col==0 or col==6 )and (row!=5 and row!=6)) or (row==5 and (col==1 or col==5)) or (row==6 and col>1 and col<5):
            print("*",end="")
        else:
            print(end=" ")
    print()


    
