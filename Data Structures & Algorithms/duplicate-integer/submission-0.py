class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value={}
        for i in nums:
            if i in value:
                value[i]=value[i]+1
            else:
                value[i]=1
        
        for i in nums:
            if (value[i]>1):
                return True

        return False
        