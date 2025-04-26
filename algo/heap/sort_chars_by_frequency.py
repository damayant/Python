class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map=Counter(nums)

        bucket=[]
        result=[]

        for _ in range(len(nums)+1):
            bucket.append([])
        
        for num , frequency in frequency_map.items():
            bucket[frequency].append(num) 

        for frequency in range(len(bucket)-1,0,-1):
            for num in bucket[frequency]:
                result.append(num)
                if len(result)==k:
                    return result
                