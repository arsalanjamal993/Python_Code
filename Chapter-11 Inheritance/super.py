class Employee:
    def __init__(self):
        print("Constructor of Employee")

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager (Programmer):
    def __init__(self):
        super().__init__()
    c = 3

# o = Employee() # Prints the a attribute
# print(o.a) # print(o.b) shhow an error as there is no b at class tribute in Employee 

# o = Programmer()
# print(o.a, o.b) 

o = Manager()
print(o.a, o.b, o.c) 