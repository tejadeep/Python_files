#program to store the exception logs in file

import logging
logging.basicConfig(filename="log.txt",level=logging.INFO)
logging.info(" ******** new information came ****** ")
try:
	x=int(input("enter the  num\n"))
	y=int(input("enter the second num\n"))
	print(x/y)
except ZeroDivisionError as msg:
	print(" its wrong reyyyyyy ",msg)
	logging.exception(msg)
except ValueError as msg:
	print("enter number rey saale",msg)
	logging.exception(msg)

logging.info(" ******************** Done **************")
