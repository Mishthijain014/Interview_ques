def Pow(x, n):
    if(n==0):
        return 0
    if(n==1):
        return x
    if(n<0):
        n = -n
        x = 1/x

    half = pow(x,n//2)

    if x%2==0:
        return half * half
    else:
        return x * half * half
    
print(pow(2,3))

    