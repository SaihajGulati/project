class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #rewrite without using more memory
        #tho copying will probably use e
        #to use less memory, instead list comprehension, use for loop with number indexes to manually set
        #is same time complexity so all good
      
        #averagish case is O(n) with O(1) extra memory since setting to neg in place, but if k is close to n then approaches nlogn time complexity

        #make negative so that when python does minheap which is all it can do, we get max heap
        #doing in place much better memory wise O(1) than list comprehension which creates copy and thus adds O(n) extra memory with same time
        for i in range(0, len(nums)):
            nums[i] = - nums[i]

        heapq.heapify(nums)
        res = 0

        #klogn time so depends on k --> k close to n size makes nlogn but if that is worst case of worst case that's p good with O(n) payoff otherwise
        for i in range(k):
            res = heapq.heappop(nums)

        #last res is the one we want since does k times, remember to switch sign since we switched them above
        return -res
