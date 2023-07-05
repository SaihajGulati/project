class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #T: O(n) M: O(n)
        minHeap = []

        #O(n) operation
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            minHeap.append([dist, x, y])

        #heapify automatically sorts by first value in array
        #O(n) operation
        heapq.heapify(minHeap)

        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res
