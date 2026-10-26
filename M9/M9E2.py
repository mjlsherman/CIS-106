def calculate(num1, num2, code):
    if code == "A":
        return num1 + num2
    elif code == "S":
        return num1 - num2
    elif code == "M":
        return num1 * num2
    elif code == "D":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation code"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
code = input("Enter operation (A, S, M, D): ").upper()

result = calculate(num1, num2, code)

print("First Number:", num1)
print("Second Number:", num2)
print("Operation:", code)
print("Result:", result)
