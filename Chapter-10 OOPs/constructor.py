class Employee:
    language = "python" # This is class attribute
    salary = 120000


    def __init__(self, name, salary, language): # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("Iam Creating an object ")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("good morning")

harry = Employee("harry", 1300000, "C##")
harry.name = "harry"
print(harry.name, harry.language, harry.salary)



 