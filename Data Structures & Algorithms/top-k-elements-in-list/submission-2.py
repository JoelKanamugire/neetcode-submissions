class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFreq = defaultdict(int)
        mostFreq2 = []
        for num in nums:
            mostFreq[num] += 1
        sorted_items = sorted(mostFreq.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            mostFreq2.append(sorted_items[i][0])
        return list(mostFreq2)