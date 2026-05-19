def Permutations(nums):
    result = []
    visited = [False] * len(nums)

    def backtracking(path):
        if(len(path)==len(nums)):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue

            path.append(nums[i])
            visited[i] = True

            backtracking(path)

            path.pop()
            visited[i] = False

    backtracking([])
    return result

print(Permutations([1,2,3]))

# Time complexity = 0(n x n!)
# Space complexity = O(n) + O(n) + O(n) = O(n)