class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        nums.sort()
        for i in range(0,n-1):
                if nums[i]==nums[i+1]:
                    return True
        return False
        # hash_map={}
        # for i in nums:
        #     if i not in hash_map:
        #         hash_map[i]=1
        #     else:
        #          return True
        # return False