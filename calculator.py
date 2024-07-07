def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error! Division by zero."

def main():
    print("Welcome to Basic Python Calculator")

    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        operations = {'1': add, '2': subtract, '3': multiply, '4': divide}
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in operations:
            result = operations[choice](num1, num2)
            print("Result:", result)
        else:
            print("Invalid input")

        another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the Basic Python Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
