#brute force method
#O(n^2) time complexity
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)) :
            for j in range(i+1, len(nums)) :
                if nums[i] == target - nums[j] :
                    return [i,j]
        return "no such combination"
