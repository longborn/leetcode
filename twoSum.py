class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new = list(nums)
        res = [0,0]
        new.sort()
        i = 0
        j = len(nums)-1
        while i<j :
            if new[i]+new[j] == target :
                a=new[i]
                print(a)
                b=new[j]
                break
            elif new[i]+new[j] <=target:
                i=i+1
            elif new[i]+new[j] >=target:
                j=j-1
        count=0
        for num in nums :
            if num == a :
                res[0] = count
                print(num)
                break
            count = count + 1
        count = 0
        for num in nums :
            if num == b and count != res[0]:
                res[1] = count
                break
            count = count + 1
        return res
            