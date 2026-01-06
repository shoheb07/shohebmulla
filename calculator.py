import math

def basic_operations():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose operation: ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid choice")


def trigonometry():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)

    print("\n1. sin")
    print("2. cos")
    print("3. tan")

    choice = input("Choose operation: ")

    if choice == "1":
        print("sin =", math.sin(rad))
    elif choice == "2":
        print("cos =", math.cos(rad))
    elif choice == "3":
        print("tan =", math.tan(rad))
    else:
        print("Invalid choice")


def logarithms():
    num = float(input("Enter number: "))

    if num <= 0:
        print("Error: Log not defined for zero or negative numbers")
        return

    print("\n1. log10")
    print("2. ln")

    choice = input("Choose operation: ")

    if choice == "1":
        print("log10 =", math.log10(num))
    elif choice == "2":
        print("ln =", math.log(num))
    else:
        print("Invalid choice")


def power_root():
    print("\n1. Power (x^y)")
    print("2. Square Root")

    choice = input("Choose operation: ")

    if choice == "1":
        x = float(input("Enter base: "))
        y = float(input("Enter exponent: "))
        print("Result:", math.pow(x, y))
    elif choice == "2":
        x = float(input("Enter number: "))
        if x >= 0:
            print("Result:", math.sqrt(x))
        else:
            print("Error: Negative number")
    else:
        print("Invalid choice")


def main():
    while True:
        print("\n=== ENGINEERING CALCULATOR ===")
        print("1. Basic Operations")
        print("2. Trigonometry")
        print("3. Logarithms")
        print("4. Power & Root")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            basic_operations()
        elif choice == "2":
            trigonometry()
        elif choice == "3":
            logarithms()
        elif choice == "4":
            power_root()
        elif choice == "5":
            print("Exiting Calculator...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
