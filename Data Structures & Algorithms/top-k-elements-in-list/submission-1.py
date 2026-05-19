class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        res = []
        for num,cnt in count.items():
            res.append([cnt, num])
        res.sort()

        arr = []
        while len(arr) < k:
            arr.append(res.pop()[1])
        return arr