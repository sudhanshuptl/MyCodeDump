"""
Problem Summary
You are given a list of meetings, where each meeting includes a name, start time, and total duration. The meetings are not necessarily sorted by any time criteria. Additionally, you have a number n, representing the number of available spaces (or auditoriums) in which the meetings can be conducted. The spaces are numbered incrementally from 0 to n-1.

Objective:
You need to determine which space hosts the maximum number of meetings and return the space number.

Constraints:
Once a meeting starts in a space, it remains there until it ends.
Meetings can be delayed if no space is available at the scheduled start time.
If multiple spaces are available for a meeting, it should choose the space with the lowest rank.
Example:
Given the meetings: {{M1, 0, 7}, {M2, 1, 5}, {M3, 4, 6}} and n = 2 (meaning there are 2 spaces available), determine the space that hosts the maximum number of meetings.

Additionally, there is a requirement to check if a room/stage is already booked at a given interval and to implement a BST iterator with functions next() and hasNext() for inorder traversal.

Detailed Example:
Consider one meeting room and two meetings [[0, 5], [1, 4]]:

The first meeting occupies the room from time 0 to 5.
The second meeting can only start at 5 and end at 8, as the room is occupied by the first meeting from 0 to 5.
Steps to Solve:
Parse and Sort Meetings:

Parse the meeting list and sort the meetings by their start time.
Schedule Meetings:

Use a min-heap to keep track of the end times of meetings in each space.
Iterate through the sorted meetings and assign them to the earliest available space or delay their start if necessary.
Track Maximum Meetings:

Maintain a count of meetings in each space.
Determine which space hosts the maximum number of meetings.
Return the Result:

If multiple spaces have the same maximum number of meetings, return the space with the smallest number.
"""

import heapq


def find_max_meetings_space(meetings, n):
    # Sort meetings by start time
    meetings.sort(key=lambda x: x[1])

    # Min-heap to track the end times of meetings in each space
    heap = []
    # Initialize counters for each space
    space_meetings_count = [0] * n

    for meeting in meetings:
        name, start, duration = meeting
        end = start + duration

        # If there's an available space, assign the meeting to it
        if len(heap) < n:
            heapq.heappush(heap, (end, len(heap)))
            space_meetings_count[len(heap) - 1] += 1
        else:
            # Check the earliest available space
            earliest_end, space = heapq.heappop(heap)
            if start >= earliest_end:
                heapq.heappush(heap, (end, space))
                space_meetings_count[space] += 1
            else:
                # Delay the meeting
                heapq.heappush(heap, (earliest_end + duration, space))
                space_meetings_count[space] += 1

    # Find the space with maximum meetings
    max_meetings = max(space_meetings_count)
    for i in range(n):
        if space_meetings_count[i] == max_meetings:
            return i


# Example usage
meetings = [["M1", 0, 7], ["M2", 1, 5], ["M3", 4, 6]]
n = 2
print(find_max_meetings_space(meetings, n))  # Output: Space number with maximum meetings

for i in range(5 - 1, -1):
    print(i)