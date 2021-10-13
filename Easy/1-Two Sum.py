class Solution:
    #brute force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums:
                if i + j == target:
                    return [nums.index(i), nums.index(j)]

    #optimised
    def o_twoSum(self, nums: List[int], target: int) -> List[int]:
        resultDict = {} #store dict/hashmap of complement of our search val

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in resultDict:
                return [i, resultDict[complement]]
            resultDict[nums[i]] = i