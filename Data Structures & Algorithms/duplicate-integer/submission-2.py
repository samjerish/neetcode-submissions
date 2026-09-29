class Solution:
    def hasDuplicate(self, nums):
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1

        for j in a.values():
            if j>1:
                return True
        else:
            return False    