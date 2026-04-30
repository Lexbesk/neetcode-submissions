class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts[num] + 1 if num in counts else 1
        list_counts = []
        for num in counts:
            list_counts.append([num, counts[num]])
        list_counts.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(list_counts[i][0])
        return res