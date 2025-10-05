class Employee:
    company = "Microhard"
    name = "Default name "
    def show(self):
        print(f"The name is  {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, coder):
    company = "swift tech"
    def showLanguage(self):
        print(f"The name is  {self.company} and the language is {self.language}")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()

print(a.company, b.company)