class Employee:
    company = "Microhard"
    def show(self):
        print(f"The name is  {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "swift tech"
    def showLanguage(self):
        print(f"The name is  {self.name} and the language is {self.language}")

a = Employee()

b = Programmer()

print(a.company, b.company)