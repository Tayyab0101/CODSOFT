def add(a, b): #add
    return a + b

def subtract(a, b): #sub
    return a - b

def multiply(a, b): #multiply
    return int(a * b)

def divide(a, b): # division
    if b == 0:
        return "Cannot Divide by Zero."
    elif a % b == 0:
        return int(a / b)
    else:
        return a / b

def calculator():
    while True:
        print("Sel Op: 1 for add, 2 for Subtract, 3 for Multiply and 4 for Division")
        choice = input("Enter operation: ")

        first_number = input("Enter first number: ")
        second_number = input("Enter second number: ")

        # Check if inputs are valid numbers
        try:
            a = float(first_number)
            b = float(second_number)
        except ValueError:
            print("Please enter a valid number.")
            continue  # Restart the loop

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

        restart = input("Do you want to calculate again? (y/n): ")
        if restart.strip().lower() != 'y':  # Check lowercase version of input
            break

calculator()
