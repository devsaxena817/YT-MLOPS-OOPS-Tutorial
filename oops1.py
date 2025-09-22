# Initialize a class
class employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
        print(id(self))
        print("I am inside constructor")
        self.id=123
        self.salary="50000"
        self.designation="SDE"
        print("I am leaving constructor")
    def travel(self):
        print("I am travel method")
        print("I am travelling to INDIA")

# create an obj/instance of the class
sam=employee()
sam.name="Sam Saxena"
print(sam.name)
# print(id(sam))
# sam1=employee()
# # sam.travel("India")
# # print(sam.salary)
# # sam.travel()
# print(id(sam1))
