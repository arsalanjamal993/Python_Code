class Employee:
    language = "python" # This is class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("good morning")

harry = Employee()
# harry.name = "harry"
# harry.language = "php"  # This is instance attribute
# print(harry.name, harry.language, harry.salary)
harry.getInfo()
harry.greet()


