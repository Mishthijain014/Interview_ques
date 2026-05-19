def comb_sum(candidates,target):
    result = []

    def backtracking(index,path,target):
        if(target==0):
            result.append(path[:])
            return
        
        if target < 0:
            return
        
        for i in range(index,len(candidates)):
            path.append(candidates[i])
            backtracking(i,path,target-candidates[i])
            path.pop()

    backtracking(0,[],target)
    return result

print(comb_sum([2,3,6,7],7))

#time complexity = O(N^T/M)
#space complexity = O(T/M)