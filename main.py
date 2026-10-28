print("Student Marks Calculator")

name = input("Enter your name: ")
mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\nStudent:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
