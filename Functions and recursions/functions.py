

success = 1

def cal_sun(a,b): #parameters
    sum = a +b
    print(sum)
    return success
 

#  function call
retval = cal_sun(12,13) #arguments

if(retval):
    print("function executed")
else:
    print("Function failed")

# if there is no return in a function then it gives None