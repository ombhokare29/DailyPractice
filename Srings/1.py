# Sting is a datatype which store the sequence of characters
str = 'Thii is a string'
str1 = "This is a string enclosed in double quotes"


# Triple quotes are used for multiline string
str2 = """ in triple quotes"""

print(str)
print(str1)
print(str2)

# escape sequnce charcters
# \n, \b ,etc


# String concatenation 
# We can concatenate two strings in python using "+"


concat_str = str + str2

print(concat_str)

print(len(str))

# Indexing
print(str[0] )


# String function

print(str.endswith('g')) #Returns true if ends with g else false

print(str.capitalize()) #capitalize the first lettre , works only one time 

print(str.replace('T','O'))  #rejplaces the old value to new value

print(str.find("Thii")) #returns the i;ndex of first occurance

print(str.count('i')) #Counts the number of occurances in a string

new = input("Enter yuout name: ")

print(new)
print("Length of your name is : ", len(new))

doll_cnt = "this is the $ count $"

print("the count of $ is", doll_cnt.count('$'))