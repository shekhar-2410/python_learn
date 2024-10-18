# ask the user to enter their three favourite movie and enter in list
movies = []
movies.append(input("Enter first movie: "))
movies.append(input("Enter second movie: "))
movies.append(input("Enter third movie: "))
print(movies)

# check if list is palindrome or not
palindrome = ["m","a","a","m"]
palindrome2 = palindrome.copy()
palindrome2.reverse()
if palindrome == palindrome2:
    print("palindrome")
else:
    print("not palindrome")


#cont the number of student with the "A" grade in the following tuple 
grades = ("C","D","A","A","B","B","A")
print(grades.count("A"))

#store the above value into a list and sort
new_list = list(grades)
new_list.sort()
print(new_list)