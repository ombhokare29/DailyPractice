

# movies = []

# for i in range(3):

#     n = input(f"Enter your favourite movie {i+1}")
#     movies.append(n)
# print(movies)



# palindrom
# :: same from front and reverse
list = []
m  = int(input("Tell me the number of elements you want in list: "))

for i in range(m):
    el = input("Enter the list element")
    list.append(el)

list1 = list.copy()
list1.reverse()

palc = 0
nopal = 0
for j in range(m):
    if(list[j] == list1[j]):
        palc +=1
    else:
        nopal = 1

if(nopal == 1):
   print("not a palindrom")

elif(palc == m):
    print("Yes, Its a palindrom")