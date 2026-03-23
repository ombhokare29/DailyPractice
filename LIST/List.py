marks = [21,32,4,56,654,3]

print(marks)
print(type(marks))


# indexing starts form 0

print(len(marks))
print(marks[0],marks[1])

# we can store data with different datatypes


student = ['name', 12, 12.00]

print(student)

# strings are immutable in python
# LIST are mutable in python 

student[0] = 'Om'

print(student)


# if we try to access the more than the available index it will throw error



# ************************************************************


# *****  LIST SLICING     ************************

mark = [12,3,55,64,7,6,4,34,3]
print(mark[1:5])




# *****  LIST Methods     ************************



list = [1,3,2,5]

list.append(4)  #adds 4 at the last ,,,his function returns None

list.sort() # sorts by ascending order,, this function returns None

list.sort(reverse=True) #sorts by descending order

print(list)
list.reverse() # reverses the list

list.insert(2, 23)
print(list)



