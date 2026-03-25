def factorial(n):
    fact = 1
    if(n==0 or n==1):
        fact = 1
    else:
        for i in range(1,n+1):
            fact = fact *i
    return fact

ans =factorial(5)
print(ans)