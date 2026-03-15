class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            index=abs(n)-1
            nums[index]=-1*abs(nums[index])

        res=[]
        for index,n in enumerate(nums):
            if n>0:
                res.append(index+1)
        return res
