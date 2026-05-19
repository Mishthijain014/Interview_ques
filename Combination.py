def Combination(k,n):
    result = []

    def backtracking(index,path):
        if(k==len(path)):
            result.append(path[:])
            return
        
        for i in range(index,n+1):
            path.append(i)
            backtracking(i+1,path)
            path.pop()
        
    backtracking(1,[])
    return result

print(Combination(2,4))

# time complexity = O(n/k)