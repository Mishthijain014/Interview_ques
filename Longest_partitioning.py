from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_partition(sub):
            return sub[::-1] == sub

        def backtracking(start,path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start,len(s)):
                substring = s[start:end+1]

                if is_partition(substring):
                    path.append(substring)
                    backtracking(end+1,path)
                    path.pop()

        backtracking(0,[])
        return result
