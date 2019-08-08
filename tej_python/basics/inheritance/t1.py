#**************************** PARENT ******************************************

class Parent:    					    # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

#************************** CHILD_1 *******************************************

class Child: # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

class Child_2(Parent,Child): # define child class
   def __init__(self):
      print ("Calling child constructor")

 


#obj3=Child_2()
obj3=Child_2()
obj2=Parent()
obj3.parentMethod()
obj3.setAttr(10)
obj3.getAttr()
obj3.childMethod()

print issubclass(Child,Parent)
print isinstance(obj2,Parent)

obj3.parentMethod()
