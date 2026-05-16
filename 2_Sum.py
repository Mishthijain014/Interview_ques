def two_sum(num,target):
    left = 0
    right = len(num) - 1

    while left < right:
        targeted_sum = num[left] + num[right]

        if targeted_sum == target:
            return[left+1,right+1]
            break

        elif targeted_sum < target:
            left += 1

        else:
            right -= 1

print(two_sum([2,7,11,15], 9))

# time complexity == O(n)   n=len of num
# space complexity === O(1)  No extra array or hashmap.