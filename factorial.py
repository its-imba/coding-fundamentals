print("Enter a number: ")
num = int(input())

fact = 1
i = 1

def factorial(x):
while i <= num:
    fact = fact * i
    i = i+1
    
print("Factorial of", num, "is", fact)