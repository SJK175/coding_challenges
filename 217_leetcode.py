# leetcode problem : 217 - contains duplicate.
# the main takeaways from this problem comes when we solve this problem with O(n) time complexity. 
# To achieve the same, we first create a hashset ane put each array object in the set. Then we check for each obejct if it already resides in the hash table.
# for more detail refer this video : https://www.youtube.com/embed/3OamzN90kPg

class Solution(object):
    def containsDuplicate(self, nums):
        hash_set = set()
        
        for i in nums :
            if i in hash_set :
                return True
            else :
                hash_set.add(i)
                
        return False    
