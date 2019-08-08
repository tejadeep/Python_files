import os
try:
	print("uffff")
#	os._exit(0)
	print(10/0)
#	os._exit(0)  #here it is not exucuted because it is below the exception raise
print("hellloooooooooo")
except ZeroDivisionError:
	print("okkkkkkkkk")
finally:
	print("yes printinggggggggg")
