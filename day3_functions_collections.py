# Day 3 Python Practice
# Learned functions, lists and dictionaries today

# Program 1: Add two numbers using a function

def add_numbers(a, b):
    return a + b

print("Sum of numbers:", add_numbers(5, 7))

print("-------------------------------")

# Program 2: Check whether a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print("Number is", check_even_odd(number))

print("-------------------------------")

# Program 3: List example

marks = [75, 82, 90, 88, 79]

print("Marks of student:")
for m in marks:
    print(m)

print("Total subjects:", len(marks))

print("-------------------------------")

# Program 4: Calculate average marks

total = 0
for m in marks:
    total = total + m

average = total / len(marks)
print("Average marks:", average)

print("-------------------------------")

# Program 5: Dictionary example

student = {
    "name": "Ankit",
    "branch": "CSE AI & ML",
    "year": 2,
    "college": "Supreme Knowledge Foundation"
}

print("Student details:")
print("Name:", student["name"])
print("Branch:", student["branch"])
print("Year:", student["year"])
print("College:", student["college"])

print("-------------------------------")

# Program 6: Loop through dictionary

for key, value in student.items():
    print(key, ":", value)
