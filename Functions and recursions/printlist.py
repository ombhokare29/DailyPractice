def printList(lst, index = 0):
    if index == len(lst):
        return
    else:
        print(lst[index])
        printList(lst,index+1)


lsit1 = ["aple",1,3,4,5]
printList(lsit1)