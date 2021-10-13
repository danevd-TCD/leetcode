class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #left look first:
        #e.g in [ 1, 2 , 3, 4]
        #we say leftArray[0] = 1, as everything left of first position is 1
        #|--> leftArray = [1]
        #leftArray[1] = nums[0] * leftArray[0] = 1 * 1 = 1 
        #|--> leftArray = [1, 1]
        #leftArray[2] = nums[1] * leftArray[1] = 2 * 1 = 2
        #|--> leftArray = [1, 1, 2]
        #leftArray[3] = nums[2] * leftArray[2] = 3 * 2 = 6
        #final leftArray:
        #|--> [1, 1, 2, 6]
        
        #then right look:
        #e.g in [ 1, 2 , 3, 4]
        #first element = nums(1 * 2 * 3 * 4)
        #second element = nums(2 * 3 * 4)
        #third element = nums(3 * 4)
        #fourth/last element = nums(4) = nums(size(nums))
        
        leftArray = []
        leftArray.append(1)
        for i in range(len(nums)-1):
            currentVal = nums[i] * leftArray[i]
            leftArray.append(currentVal)
        
        print(leftArray)
        
        reversedNums = []
        for i in range(len(nums)-1,-1,-1):
            reversedNums.append(nums[i])
        
        rightArray=[]
        rightArray.append(1)
        for i in range(len(reversedNums)-1):
            #print(reversedNums[i])
            currentVal = reversedNums[i] * rightArray[i]
            rightArray.append(currentVal)
            
        
        reversedRightArray = []
        for i in range(len(rightArray)-1,-1,-1):
            reversedRightArray.append(rightArray[i])
        
        print(reversedRightArray)
        
        answerArray = []
        for i in range(len(leftArray)):
            answerArray.append(leftArray[i] * reversedRightArray[i])
            
        print(answerArray)
        return answerArray