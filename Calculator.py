a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Choose math operation (+, -, *, /): ")

if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)
else:
    print("You did not provide correct math operation!")