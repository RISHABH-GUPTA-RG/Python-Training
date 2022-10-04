import math

num=int(input("Enter the number:-> "))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
    print((math.factorial(int(num))))

input()