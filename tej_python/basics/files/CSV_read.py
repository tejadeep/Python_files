import csv
f=open("excel_demo.csv","r")
r=csv.reader(f)
data=list(r)
for line in data:
	for word in line:
		for char in word:
			print (char)
			print("*********")
f.close()
