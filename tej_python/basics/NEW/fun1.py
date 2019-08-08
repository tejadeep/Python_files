var=10
def func1():
	global var
	var=9
	var=var+1
	print("var value in func1 is ",var)
	return
func1()
