class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value={}
        for i in nums:
            value[i]=value.get(i,0)+1
        
        for i in value:
            if value[i]>1:
                return True

        return False
        