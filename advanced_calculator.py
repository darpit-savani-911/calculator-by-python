# ==========================================
# Advanced Calculator Project in Python
# Created for learning Python basics
# This calculator supports many operations
# ==========================================

import math   # Importing math module for square root and power

# Function to display the calculator menu
def show_menu():
    print("\n==============================")
    print("        PYTHON CALCULATOR     ")
    print("==============================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Percentage (%)")
    print("8. Exit")
    print("==============================")

# Function for addition
def addition():
    print("\n--- Addition ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a + b
    print("Result:", result)

# Function for subtraction
def subtraction():
    print("\n--- Subtraction ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a - b
    print("Result:", result)

# Function for multiplication
def multiplication():
    print("\n--- Multiplication ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a * b
    print("Result:", result)

# Function for division
def division():
    print("\n--- Division ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = a / b
        print("Result:", result)

# Function for power
def power():
    print("\n--- Power ---")
    base = float(input("Enter base number: "))
    exponent = float(input("Enter exponent: "))
    result = math.pow(base, exponent)
    print("Result:", result)

# Function for square root
def square_root():
    print("\n--- Square Root ---")
    number = float(input("Enter number: "))

    if number < 0:
        print("Error: Cannot calculate square root of negative number.")
    else:
        result = math.sqrt(number)
        print("Result:", result)

# Function for percentage
def percentage():
    print("\n--- Percentage ---")
    value = float(input("Enter value: "))
    percent = float(input("Enter percentage: "))
    result = (value * percent) / 100
    print("Result:", result)

# Main program loop
while True:

    # Display menu
    show_menu()

    # User choice
    choice = input("Enter your choice (1-8): ")

    # Checking user choice
    if choice == "1":
        addition()

    elif choice == "2":
        subtraction()

    elif choice == "3":
        multiplication()

    elif choice == "4":
        division()

    elif choice == "5":
        power()

    elif choice == "6":
        square_root()

    elif choice == "7":
        percentage()

    elif choice == "8":
        print("\nThank you for using Python Calculator.")
        print("Program Closed.")
        break

    else:
        print("\nInvalid choice. Please select a valid option.")
