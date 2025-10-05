try:
    a = int(input("Enter a: ")) 
    b = int(input("Enter b: "))
    a/b
except ZeroDivisionError as v:
    print("Infinite")
