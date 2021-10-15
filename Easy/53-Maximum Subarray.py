class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """aka kadane's algorithm"""
        maxSum = 0
        curSum = 0
        
        for number in nums:
            #current sum val is either 0, aka "do not add to maxSum, instead reset",
            #or, curSum + number
            curSum = max(0, curSum + number)
            
            #curSum's result thus either resets maxSum to 0
            #or adds to it
            maxSum = max(maxSum, curSum)
        
        return maxSum