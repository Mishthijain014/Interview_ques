def comb_sum(candidates,target):
    candidates.sort()
    result = []

    def backtracking(index,path,target):
        if target == 0:
            result.append(path[:])
            return
        
        if target < 0:
            return
        
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue

            path.append(candidates[i])
            backtracking(i+1,path,target-candidates[i])
            path.pop()

    backtracking(0,[],target)
    return result

print(comb_sum([10,1,2,7,6,1,5],8))

# time complexity = O(2n×k)
# space complexity = O(n)