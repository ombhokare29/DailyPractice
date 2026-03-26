def find_sum(n):
    if n==0 :
        return 0
    else:
        return n + find_sum(n-1)
    
print(find_sum(100))


def addi(n):
    sum = 0
    if(n == 0):
        return 0
    else:
        for i in range(n+1):
            sum = sum +i
            

    return sum

print(addi(2873160))