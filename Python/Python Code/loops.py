# name = "Amin Islam"
# age = 23

# if age >= 18:
#     print(name + " you are adult")


# # x = 1
# # while x <= 10:
# #     print( x )    
# #     x += 1

# # y = 1
# # while y <= 3:
# #     z = 1
# #     while z <= 3:
# #         print("y :", y, "z :", z)
# #         z += 1
# #     y += 1    


# password = ""
# while password != "admin123":
#     password = input("Enter the password: ")
# print("Access granted!") 


# # while True:
# #     number = int(input("Enter a number (0 to exit): "))
# #     if number == 0:
# #         break
# #     print("You entered:", number)


# a = 1 
# while a <= 10:
#     print(a)
#     a = a + 2
       
# b = 1
# while b <= 10:
#    if b % 2 == 0:
#     print(b)
#     b = b + 2

# x  = 20
# while x > 0:
#    print(x)
#    x -= 1

while True:
   name = input("Enter your name: ")
   if name.lower() == "exit":
      break
   print("Hello, " + name + "!")       