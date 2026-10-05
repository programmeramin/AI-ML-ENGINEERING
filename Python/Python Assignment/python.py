#=====================================================
# Question 1: Simple Function with Parameters
#=====================================================

def calculate_area(length, width):
    return length * width

result = calculate_area(5, 4)

print(f"The area of the rectangle is: {result}")


#======================================================
# Question 2: Greeting Function with Default Parameter
#======================================================

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Amin"))
print(greet("Amin", "Good Morning"))


#=======================================================
# Question 3: Using Built-in Module
#=============================================

import math

square_root = math.sqrt(25)
power = math.pow(2, 3)

print(f"Square root of 25 is: {square_root}")
print(f"2 raised to the power 3 is: {power}")

#=======================================================
# Question 4: File Handling (Write and Read)
#=======================================================
file_name = open("sample.txt", "w")

file_name.write("Welcome to Python Programming!")

file_name.close()

file_name = open("sample.txt", "r")

content = file_name.read()

print(f"Content of the file: {content}")


#=============================================
# Question 5: OOP Basics (Class and Object)
#=============================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")


student1 = Student("Ayesha", 92)

student1.display_info()

