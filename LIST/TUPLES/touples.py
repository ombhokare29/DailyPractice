tup = (1,2,3,43,4,5,65,2)

#immutable 
#allows immutable sequence of items 

print(tup)

print(type(tup))

#we can access the items at various indexes but cannot modify it
single_valu_tuple = (1,)


# for si;ngle valued tuple always add a comma otherwise it willbehave a  thedatatype of the element 

# tuple slicing is possible

cnt=tup.count(2)

print(cnt)


tuple1 = ['c','a','b','c','a','a']

# dj = tuple1.count('a')
# print(dj)
tuple1.sort(reverse= True)

print(tuple1)