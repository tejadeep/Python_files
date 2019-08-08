class god:
	a=10
	def __init__(self,name,marks):
		print name
		print marks
		self.name="hariiii"
		self._marks=30
		self.__roll=220
		print self.name
		print self._marks
		print self.__roll
		print "helllooooo"

obj=god("tej",56)
#obj.name=50
print "*******************************"
print obj.name
print obj._marks
#print obj.__roll
