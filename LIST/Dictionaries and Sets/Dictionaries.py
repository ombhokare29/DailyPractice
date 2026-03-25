# dictionaries stores the key value pairs

# key:value

# unordered, mutable band no duplicate keys

info  = {
    "name" : "om",
    "id" : 12
}
print(info)

print(info["name"])

info["name"] = "Raja"
info["surname"] = "singh"

print(info["name"])
print(info["surname"])


print("*****************************************************\n\n")



#  nested dictionaries

school = {
    "name" : "om",
    "Subject" : {
        "chem" : 32,
        "math" : 100,
        "Phy" : 59
    }
}

print(school)
print(school["Subject"])
print(school["Subject"]["math"])


print("*****************************************************\n\n")

print(school.keys())

# print(list(school.keys()))

print(school.items())