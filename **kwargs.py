# this is used for multiple named arguments


def info(**kwargs):
    print(kwargs)

info(name = "Om", skill = "python")


# kwargs will print the data in the form of dictionaries
