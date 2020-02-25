import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # by deafult heapq in python is a min-heap
        # but we require max-heap so we need to convert every
        # value to negative to convert smallest value to biggest
        stones = [-1*i for i in stones]
        # heapify() to convert list to maxheap
        # so first index of list will be the maximum of all
        heapq.heapify(stones)
        while(len(stones)>=2):
            # print(stones)
            # take the first two elements
            num1 = heapq.heappop(stones)
            num2 = heapq.heappop(stones)
            # check the difference if it found to be 0 then the two stone 
            # are completely destroyed so no need to add back to list
            if((num1-num2)!=0):
                heapq.heappush(stones,num1-num2)
                heapq.heapify(stones)
        # finally convert negative to positive and return
        if(len(stones)):
            return stones[0]*-1
        else:
            return 0
                