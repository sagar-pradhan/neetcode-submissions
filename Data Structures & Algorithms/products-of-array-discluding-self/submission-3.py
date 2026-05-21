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
                if c:
                    res[i]=0
                else:
                    res[i] = prod
            else:
                res[i]=prod//c
        
        return res