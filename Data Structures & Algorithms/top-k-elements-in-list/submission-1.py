class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        seen = {}
        heap = []
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for num, freq in seen.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
