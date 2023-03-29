num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))

choices = """
1. Add +
2. Subtract -
3. Multiply *
4. Divide /
5. Square ^
"""

print(choices)

calc = int(input("Choose an operation's number to perform: "))


if calc == 1:
    operation = num1 + num2
    print(num1, "+", num2, " = ", operation)

elif calc == 2:
    operation = num1 - num2
    print(num1, "-", num2, " = ", operation)
    
elif calc == 3:
    operation = num1 * num2
    print(num1, "*", num2, " = ", operation)
    
elif calc == 4:
    operation = num1 / num2
    print(num1, "/", num2, " = ", operation)
    
elif calc == 5:
    operation = num1 ** num2
    print(num1, "^", num2, " = ", operation)
    
else:
    print("Please select a number from 1-5 to use the correct operator") 
   


