class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)) :
            try :
                x=nums[i]
            except IndexError :
                break 
            if nums[i] == 0 :
                count = count + 1 
                nums.remove(0)
                i=i-1
                
        for i in range(count) :
            nums.append(0)
        return None
                
        