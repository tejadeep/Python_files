try:
	x=int(input("enter the number"))
	y=int(input("enter the other number"))
	print(x/y)
except ArithmeticError:
	print("Arthmatic errorr\n")
except ZeroDivisionError:
	print("zero division error\n")
