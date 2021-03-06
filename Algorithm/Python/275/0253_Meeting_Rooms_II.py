'''

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

'''

# approach 1: using heap

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        intervals.sort()

        # Add the first meeting
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:
            # If the earliest end time <= current meeting start time, 
            # so we can add current meeting to current rooms, pop previous end time
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

# approach 2

# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:       
#         # If there are no meetings, we don't need any rooms.
#         if not intervals:
#             return 0

#         used_rooms = 0

#         # Separate out the start and the end timings and sort them individually.
#         start_timings = sorted([i[0] for i in intervals])
#         end_timings = sorted(i[1] for i in intervals)
#         L = len(intervals)

#         # The two pointers in the algorithm: e_ptr and s_ptr.
#         end_pointer = 0
#         start_pointer = 0

#         # Until all the meetings have been processed
#         while start_pointer < L:
#             # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
#             if start_timings[start_pointer] >= end_timings[end_pointer]:
#                 # Free up a room and increment the end_pointer.
#                 used_rooms -= 1
#                 end_pointer += 1

#             # We do this irrespective of whether a room frees up or not.
#             # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
#             # remain the same in that case. If no room was free, then this would increase used_rooms
#             used_rooms += 1    
#             start_pointer += 1   

#         return used_rooms





