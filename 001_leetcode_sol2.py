#solution-02
# time complexity O(N)
class Solution(object):
    def twoSum(self, nums, target):
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = i
            
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashtable and hashtable[complement] != i:
                return [i, hashtable[complement]]
