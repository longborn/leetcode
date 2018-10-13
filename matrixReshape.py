class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        temp = []
        res = []
        for i in nums :
            temp.extend(i)
        if len(temp) == r*c :
            for i in range(r) :
                x = []
                for j in range(c) :
                    x.append(temp[i*c+j])
                res.append(x)
        else :
            return nums 
        return res 