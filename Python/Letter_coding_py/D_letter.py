for row in range(7):
    for col in range(7):
        if ((row==0 or row==6 )and (col!=5 and col!=6)) or ((row==1 or row==5) and col==5) or (col==6 and (row>1 and row<5)) or (col==1 and (row>0 and row<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
