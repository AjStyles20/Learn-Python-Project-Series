def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    if y == 0:
        return "Error: Division by zero"
    return x / y 

print("=== Simple Calculator ===")
print("Choose Operation:")
print("1. Add (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

Operation = input("Enter Your Choice (+, -, *, /): ")

Num1 = float(input("Enter Your First Number: "))
Num2 = float(input("Enter Your Second Number: "))

if Operation == '+':
    result = add(Num1,Num2)
elif Operation == '-':
    result = subtract(Num1,Num2)
elif Operation == '*':
    result = multiplication(Num1, Num2)
elif Operation == '/':
    result = division(Num1,Num2)
else:
    result = "Invalid Operation"
print("Result:", result)


