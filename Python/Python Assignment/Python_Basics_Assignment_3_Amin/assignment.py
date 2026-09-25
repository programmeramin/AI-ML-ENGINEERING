#----------------------------------
# Question 1: Enumerate with List
#___________________________________

fruits = ["apple", "banana", "cherry", "mango"]

for index, fruit in enumerate(fruits):
  print(index, fruit)

#--------------------------------------
# Question 2: Zip with Two Lists
#--------------------------------------

students = ["Rahim", "Karim", "Ayesha"]

scores = [85, 90, 78]

for student, score in zip(students, scores):
  print(student, score)

#-----------------------------------
# Question 3: Tuple and Loop
#-----------------------------------

subjects = ("Math", "English", "Physics", "Chemistry", "Biology")

for subject in subjects:
  print(subject)

#-----------------------------------
# Question 4: Set Operations
#-----------------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Common elements
print(set1.intersection(set2))

# Unique elements of set1
print(set1.difference(set2))

#--------------------------------------
# Question 5: Dictionary with Enumerate
#--------------------------------------

marks = {
    "Math" : 80,
    "Physics" : 75,
    "Chemistry" : 85
}


for number, (subject, mark) in enumerate(marks.items(), start=1):
  print(number, subject + ":", mark)

