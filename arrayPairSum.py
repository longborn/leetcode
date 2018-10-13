class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i,num  in enumerate(nums) :
            if i%2 == 0 :
                res = res + num 
        return res 
        