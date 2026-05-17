def three_Sum_Closest(nums,target):
    nums.sort()

    closest_sum = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)-2):

        left = i+1
        right = len(nums) - 1

        while left < right:
            
            curr_sum =  nums[i] + nums[left] + nums[right]

            if abs(target - curr_sum) < abs(target - closest_sum):
                closest_sum = curr_sum

            if curr_sum < target:
                left += 1

            elif curr_sum > target:
                right -= 1

            else:
                return closest_sum
            
    return closest_sum

print(three_Sum_Closest([-1,2,1,-4],1))

# time complexity = O(n^2)
# space complexity = 0(1)
