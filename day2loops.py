# Day 2: Python Loops and Conditions Practice
# Author: Ankit Singh
# Topic: if-else, for loop, while loop

# Program 1: Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("----------------------------")

# Program 2: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print("----------------------------")

# Program 3: Multiplication Table
n = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print("----------------------------")

# Program 4: Sum of first N numbers
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)

print("----------------------------")

# Program 5: While loop example
i = 1
while i <= 5:
    print("Hello", i)
    i += 1
