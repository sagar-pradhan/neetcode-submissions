class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prod=1
        cnt = 0
        for num in nums:
            if num == 0:
                cnt+=1
            else:
                prod*=num
        if cnt>1:
            return [0]*len(nums)
        
        for i,c in enumerate(nums):
            if cnt:
                res[i]=0 if c else prod
            else:
                res[i]=prod//c
        
        return res