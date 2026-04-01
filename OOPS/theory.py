# to majp with real life entities we use objests

# to reduce the redundancyt and increase the reusability
# ##CLASSES AND OBJECTS

# class is a blueprint for creating objects


# class Student:
#     name = "OM"


# # creeat;ing an object(instance)
# o1 = Student()
# print(o1.name)



class Student:

    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("Adding the new student")



s1 = Student("om",99)
s2 = Student("sai", 80)
 
print(s1.name,s1.marks)
print(s2.name,s2.marks)

# self is the reference to the current instance of a class

# self.name = name -=----Instance Variable


# Class Variable
"""lass Car:
    wheels = 4
"""