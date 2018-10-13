class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i,num in enumerate(nums) :
            if num == 0 :
                count = count + 1 
            else :
                nums[i-count] = num
                if count > 0 :
                    nums[i] = 0 
        return None
                
        