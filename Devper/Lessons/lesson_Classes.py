# Accessing Object Variables
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")
myobjectx = MyClass()
myobjectx.variable

myobjecty = MyClass()
myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)
#Accessing Object Functions
myobjectx.function()

# init()
class NumberHolder:
   def __init__(self, number):
       self.number = number
   def returnNumber(self):
       return self.number
var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'
