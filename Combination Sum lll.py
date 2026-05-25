from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtracking(index,path,target):
            if(target == 0) and len(path) ==k:
                result.append(path[:])
                return

            if target < 0:
                return
 
            for i in range(index,10):
                path.append(i)
                backtracking(i+1,path,target-i)
                path.pop()

        backtracking(1,[],n)
        return result
        