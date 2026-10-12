def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def percentage(a, b):
    if b == 0:
        return "Error! Total cannot be zero."
    return (a / b) * 100


while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Calculator closed. Goodbye!")
        break

    elif choice == "5":
        number = int(input("Enter a number: "))
        print("Result:", even_odd(number))

    elif choice in ["1", "2", "3", "4", "6"]:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if choice == "1":
            print("Result:", addition(a, b))

        elif choice == "2":
            print("Result:", subtraction(a, b))

        elif choice == "3":
            print("Result:", multiplication(a, b))

        elif choice == "4":
            print("Result:", division(a, b))

        elif choice == "6":
            print("Percentage:", percentage(a, b), "%")

    else:
        print("Invalid choice! Please select 1-7.")
