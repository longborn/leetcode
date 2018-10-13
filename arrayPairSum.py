class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = list(nums)
        temp.sort()
        res = 0
        for i,num  in enumerate(temp) :
            if i%2 == 0 :
                res = res + num 
        return res 
        