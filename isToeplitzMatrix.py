class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        temp = 0
        for i in range(rows) :
            temp = matrix[i][0]
            x = 0
            while (i < rows and x < cols) :
                if temp != matrix[i][x] :
                    return False 
                i +=1
                x +=1
        for i in range(cols) :
            temp = matrix[0][i]
            x = 0
            while (i < cols and x < rows) :
                if temp != matrix[x][i] :
                    return False
                i +=1
                x +=1
        return True
                    
                    