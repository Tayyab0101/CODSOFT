def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = a * b
    return int(result) if result.is_integer() else result

def divide(a, b):
    if b == 0:
        return "Cannot Divide by Zero."
    elif a % b == 0:
        return int(a / b)
    else:
        return a / b

def calculator():
    print("Calculator!!!")
    print("Sel Op:1 for add, 2 for Subtract, 3 for Multiply and 4 for Division")
    
    choice = input("Enter operation: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    else:
        print("Invalid input")

calculator()
