# this is used for multiple named arguments


def info(**kwargs):
    print(kwargs)

info(name = "Om", skill = "python")