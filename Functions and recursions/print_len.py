cities = ['latur','solapur','pune','mumbai']

def cal_len(list):
    print(len(list))

cal_len(cities)

def single_line(list):
    for i in range(len(list)):
        print(list[i], end= " ")

single_line(cities)

def print_list(list):
    
    for item in list:
        print(item,end = " ")

print_list(cities)