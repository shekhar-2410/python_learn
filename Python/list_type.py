# list 
marks = [10, 20, 30, 40, 50]
print(marks)
print (type(marks))
print(len(marks))

#strings are immutable
'''
name = "Sachin"
name[0] = "s"
print(name[0])
'''

#list are mutable
marks[0] = 100
print(marks)

#append list
marks.append(60)
print(marks)

#sort list
marks.sort()
print(marks)

marks.sort(reverse = True)
print(marks)

#reverse list
marks.reverse()
print(marks)


#extend list
marks.extend([70,80,90])
print(marks)

#remove list
marks.remove(100)
print(marks)

#inert list
marks.insert(len(marks),100)
print(marks)

#pop list
# marks.pop() #removes last element/or index
marks.pop(0)
print(marks)

#push list
marks.append(100) #adds last element
print(marks)