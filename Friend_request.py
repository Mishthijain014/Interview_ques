from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0]*121
        for age in ages:
            count[age] += 1

        res = 0

        for ageA in range(1,121):
            if count[ageA] == 0:
                continue

            for ageB in range(1,121):
                if count[ageB] == 0:
                    continue

                if ageB <= 0.5 * ageA + 7:
                    continue

                if ageB > ageA:
                    continue

                if  ageB > 100 and ageA < 100:
                    continue

                if ageA == ageB:
                    res += count[ageA] * (count[ageA] - 1)

                else:
                    res += count[ageA] * count[ageB]

        return res