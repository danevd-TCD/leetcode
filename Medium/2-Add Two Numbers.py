# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = [] #array for linked list 1
        list2 = [] #array for linled list 2
        
        current1 = l1
        current2 = l2
        
        print(current1)
        #print(current.next)
        
        #current = current.next
        
        #print(current.val)
        
        #list 1
        while current1.next != None:
            #print("Current val: " + str(current1.val))
            list1.append(current1.val)
            current1 = current1.next
        
        list1.append(current1.val)
        
        #list 2
        while current2.next != None:
            #print("Current val: " + str(current2.val))
            list2.append(current2.val)
            current2 = current2.next
        
        list2.append(current2.val)
        
        #reverse list 1:
        end1 = len(list1) -1
        str1 = ""
        
        for i in range(end1,-1,-1):
            str1 += str(list1[i])
        
        #reverse list 2:
        end2 = len(list2) -1
        str2 = ""
        
        for j in range(end2,-1,-1):
            str2 += str(list2[j])
        
        #sum and convert sum to string
        outputSum = int(str1) + int(str2)
        outputString = str(outputSum)
        
        #reverse the outputString
        endStringLen = len(outputString) - 1
        reversedOutput = ""
        
        for k in range(endStringLen, -1, -1):
            reversedOutput += str(outputString[k])
            
        print(reversedOutput)
        
        #ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
        
        current = ListNode()
        
        for i in range(len(reversedOutput)):
            current = current.next
            current.val = reversedOutput[i]  #this works
            #print(current.val)              #as evidenced by this: 7, 0, 8
            
            #issue is somewhere here
            current.next = ListNode()
            
            
        print(current)
        
        #create list

        
        