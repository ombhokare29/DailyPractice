def fact(n):
    if(n==0 or n==1):
        ans = 1
        return ans
    else:
        ans = n * fact(n-1)
        return ans

print(fact(5))