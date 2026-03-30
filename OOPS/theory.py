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

    def __init__(self,fullname):
        self.name = fullname
        print("Adding the new student")



s1 = Student("om")

print(s1.name)