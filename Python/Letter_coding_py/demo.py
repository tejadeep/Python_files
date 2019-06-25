from random import randint
low=int(input("enter min:"))
high=int(input("enter max"))
a=[randint(low,high) for i in range(10)]
print(a)
