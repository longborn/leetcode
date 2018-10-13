class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        for num in nums :
            if count == 0 :
                temp = num
                count = 1
            elif temp == num :
                count = count + 1 
            else :
                count = count - 1
        return temp 
                
            
            