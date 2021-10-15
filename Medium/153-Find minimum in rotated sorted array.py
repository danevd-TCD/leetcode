def findMin(nums):
    #this was my first accepted solution :)
    print("---Nums: " + str(nums) + "\n")
    first = 0
    last = len(nums) - 1
    
    midpoint = (first + last) // 2

    while first <= last:
        midpoint = (first + last) // 2

        print("|--> First: " + str(nums[first]) +"\n|--> Last: " + str(nums[last]) + "\n|--> Mid: " + str(nums[midpoint]))

        if nums[midpoint] < nums[midpoint-1]:
            print("breaker situation")
            return nums[midpoint]

        if nums[first] > nums[last]:
            first = midpoint + 1
            print("Case 1: Updating first to " + str(nums[first]))
        else:
            last = midpoint -1
            first = midpoint // 2
            print("Case 2: Updating last to " + str(nums[last]))

        

    return nums[midpoint]
        


#print(findMin([4,5,6,7,0,1,2]))
#print(findMin([5,1,2,3,4]))