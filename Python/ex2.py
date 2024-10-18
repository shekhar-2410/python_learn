# check user is entering even or odd num
num = int(input("Enter number:"))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# find the greatest of 3 numbers given by user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    result = "num1 is the greater"+" " + str(num1)
elif num2 > num1 and num2 > num3:
    result = "num2 is the greater"+" " + str(num2)
else:
    result = "num3 is the greater" +" "+ str(num3)

print(result)  

#check if number of multiple of 7 or not 
checkno = int(input("Enter number: "))
if checkno % 7 ==0:
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")