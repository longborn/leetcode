class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        size = len(a)
        i = int(size/2)-1
        for k in range(0,i+1) :
            if a[k] !=a[size-k-1] :
                return False
        return True 
        