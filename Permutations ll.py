def permutations(nums):
    nums.sort()
    result = []
    visited = [False] * len(nums)

    def backtracking(path):
        if(len(nums)==len(path)):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue

            if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue

            path.append(nums[i])
            visited[i] = True

            backtracking(path)

            path.pop()
            visited[i] = False

    backtracking([])
    return result

print(permutations([1,1,3]))
    

