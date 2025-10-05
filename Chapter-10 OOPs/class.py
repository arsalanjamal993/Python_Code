class Employee:
    language = "python" # This is class attribute
    salary = 120000

harry = Employee()
harry.name = "harry"
harry.language = "php"  # This is instance attribute
print(harry.name, harry.language, harry.salary)

arsalan = Employee()
arsalan.name = "arsalan jamal"
print(arsalan.name, arsalan.language, arsalan.salary)

