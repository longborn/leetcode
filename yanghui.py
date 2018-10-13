class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if   numRows == 0 :
            res = []
        elif numRows == 1 :
            res = [[1]]
        elif numRows == 2:
            res = [[1],[1,1]]
        else :
            res = [[1],[1,1]]
            for i in range(2,numRows) :
                temp = [1]
                for j in range(0,i-1) :
                   temp.append(res[i-1][j+1]+res[i-1][j])
                temp.append(1)
                res.append(temp)
        return res 