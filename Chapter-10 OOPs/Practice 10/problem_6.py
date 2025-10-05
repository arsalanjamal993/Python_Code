# Parent class
class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        return f"{self.name} logged in"

# Child class (inherits from User)
class Admin(User):
    def manage_website(self):
        return f"{self.name} can manage the website"

# Child class (inherits from User)
class Customer(User):
    def buy_product(self):
        return f"{self.name} can buy products"

# Creating objects
admin = Admin("Alice")
customer = Customer("Bob")

print(admin.login())         # Alice logged in
print(admin.manage_website()) # Alice can manage the website

print(customer.login())      # Bob logged in
print(customer.buy_product()) # Bob can buy products
