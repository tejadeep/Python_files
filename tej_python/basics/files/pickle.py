import pickle
class tej:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		print(self.a,self.b)
with open("pick.dat","wb") as f:
	e=tej(12,34)
	pickle.dump(e,f)
	print (" ***** pickling done ********")

with open("pick.dat","rb") as f:
	obj=pickle.load(f)
	print ("*********** unpickling done *******")
	obj.display()
