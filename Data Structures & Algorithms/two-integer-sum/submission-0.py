class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}

        for i,num in enumerate(nums):
            other_sum = target - num

            if other_sum in mpp:
                return [mpp[other_sum],i]
            else:
                mpp[num] = i
        
        