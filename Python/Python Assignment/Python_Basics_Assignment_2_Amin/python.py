#=======================================
#    Question 1: Loop Basics (for loop)
#=======================================
for i in range(1, 11):
    print(i)

#=======================================
#    Question 2: Loop with Condition
#=======================================
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")


#=======================================
#   Question 3: String Manipulation
#=======================================

# Take input from the user
text = input("Enter a string: ")

# 1. Print the string in uppercase
print("Uppercase:", text.upper())

# 2. Print the length of the string
print("Length:", len(text))

# 3. Print the string reversed
print("Reversed:", text[::-1])


#=======================================
#  Question 4: String Processing with Loop
#=======================================
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)