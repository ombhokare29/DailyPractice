def fact(n):
    if(n==0 or n==1): #base case
        ans = 1
        return ans
    else:
        ans = n * fact(n-1)
        return ans

print(fact(1000))

# while using recursions always write the code to stop at some time