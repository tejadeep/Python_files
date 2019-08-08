class Employee:
  
   'Common base class for all employees'
 
   empCount=0

   def __init__(self, name, salary):
      self.name = name
      self.hari = salary
  #    Employee.empCount += 1

      Employee.empCount+=3
      print "********************************",Employee.empCount
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.hari

obj=Employee("sanjay",1000000)
obj.displayCount()
obj.displayEmployee()
print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7"
obj.hari="modified "
print obj.hari
