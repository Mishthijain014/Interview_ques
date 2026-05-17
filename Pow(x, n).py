def Pow(x, n):
    if(n==0):
        return 1
    if(n==1):
        return x
    if(n<0):
        n = -n
        x = 1/x

    half = pow(x,n//2)

    if n%2==0:
        return half * half
    else:
        return x * half * half
    
print(pow(2,3))

# time complexity = O(logn)
# space complexity = 0(logn) 