class Animal:
    pass

class Pets:
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!")


d = Dog()

d.bark()
    