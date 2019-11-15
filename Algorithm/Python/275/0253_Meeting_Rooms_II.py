'''

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        heap = []
        intervals.sort()
        
        heapq.heappush(heap, intervals[0][1])
        
        for item in intervals[1:]:
            if heap[0] <= item[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, item[1])
            
        return len(heap)



