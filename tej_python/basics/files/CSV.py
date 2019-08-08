import csv
with open("excel_demo.csv","w",newline="") as f:
	w=csv.writer(f)
	w.writerow(["tejj","hari","hema","moni"])
	tej=1091
	hari=1089
	hema=1092
	moni=1095
	w.writerow([tej,hari,hema,moni])
print ("************* done **********")
#r=csv.reader(f)
#data=list(r)
#print (data)
#print (r)
