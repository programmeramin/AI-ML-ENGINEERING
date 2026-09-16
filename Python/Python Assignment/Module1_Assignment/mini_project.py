# ==========================================================
# Question 1: Simple Calculator Program
# ==========================================================

# Step A: Input & Setup
# Taking two numbers as input from the user and converting them to floats
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step B: Calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (Division by zero)"

# Step B (continued) & C: Displaying clearly labeled outputs
print("\n--- CALCULATOR RESULTS ---")
print(f"Addition ({num1} + {num2})       : {addition}")
print(f"Subtraction ({num1} - {num2})    : {subtraction}")
print(f"Multiplication ({num1} * {num2}) : {multiplication}")
print(f"Division ({num1} / {num2})       : {division}")

# ==========================================================
# Question 2: User Introduction Program
# ==========================================================

# Step A: Collecting user information
user_name = input("Enter your name: ")
user_city = input("Enter your city: ")
user_hobby = input("Enter your favourite hobby: ")

# Step B & C: Formatting and printing the introduction sentence using an f-string
print("\n--- USER INTRODUCTION ---")
print(f"Hello {user_name}! You live in {user_city} and you enjoy {user_hobby}.")


# ==========================================================
# Question 3: Temperature Converter (Celsius to Fahrenheit)
# ==========================================================

# Step A: Input temperature in Celsius and convert to float
celsius = float(input("Enter temperature in Celsius: "))

# Step B: Formula calculation F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Step C: Formatted output
print("\n--- TEMPERATURE CONVERSION ---")
print(f"Temperature in Fahrenheit is: {fahrenheit}°F")


# ==========================================================
# Question 4: Billing Program
# ==========================================================

# Step A: Collecting inputs for item details
item_name = input("Enter the item name: ")
price = float(input("Enter the item price: "))
quantity = int(input("Enter the quantity: "))

# Step B: Calculating total bill amount
total_bill = price * quantity

# Step C: Output bill generation with clean formatting
print("\n--- SHOPPING BILL ---")
print(f"Total Bill for {item_name} = {total_bill:.2f}")


# ==========================================================
# Question 5: Student Information Card
# ==========================================================

# Step A: Collecting student details from user
student_name = input("Enter Student Name: ")
class_section = input("Enter Class and Section (e.g., 8B): ")
school_name = input("Enter School Name: ")

# Step B & C: Printing formatted ID card using multi-line f-string and alignment
print("\n" + "-" * 28)
print("----- STUDENT ID CARD -----")
print(f"Name: {student_name}")
print(f"Class: {class_section}")
print(f"School: {school_name}")
print("----------------------------")