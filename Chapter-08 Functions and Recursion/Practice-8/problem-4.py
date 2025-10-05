'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 + 1
factorial(3) = 3 + 2 + 1
factorial(4) = 4 + 3 + 2 + 1
factorial(5) = 5 + 4 + 3 + 2 +1
factorial(n) = n + n-1 +......3 + 2 + 1

factorial(n) = n * factorial(n-1)
'''

def sum(n):
    if(n==1):
        return 1 
    return sum (n-1) + n    

print(sum(4))