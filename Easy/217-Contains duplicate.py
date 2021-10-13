class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #add all to dict
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = i
                
        return False