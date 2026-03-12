class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=len(nums)
        dict={}
        for i in range(0,x):
            ans=target-nums[i]
            if ans in dict:
                return [dict[ans],i]
            dict[nums[i]]=i