class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in match:
                return [match[x], i]
            else:
                match[nums[i]]=i
        