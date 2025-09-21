# Initialize a class
class employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
        print("I am inside constructor")
        self.id=123
        self.salary="50000"
        self.designation="SDE"
        print("I am leaving constructor")
    def travel(self,destination):
        print("I am travel method")
        print("I am travelling to ",destination)

# create an obj/instance of the class
sam=employee()
# sam.travel("India")
# print(sam.salary)
# sam.travel("India")
print(type(sam))