def add(*args):
    print(args)


add(11,2,3,4,44)


# this is the functionality in python which allows you to take as many inputs you want in a function

# example

def addition(*args):
    total =0
    for num in args:

        total += num

  
    return total


x= addition(12,12,13,4,2)

print(x)
