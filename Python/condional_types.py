age = 55
if age >= 18:
    print("You are eligible for driving license")
elif age == 17:
 print("Next year you will be eligible")
else:
    print("You are not eligible for driving license")


marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
elif marks >= 60 and marks < 70:
    grade = "D"
elif marks >= 33 and marks < 60:
    grade = "E"
else:
    grade = "You have failed the exam"


print("Your grade is", grade)
    

























