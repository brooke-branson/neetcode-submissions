"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_meets = sorted(intervals, key=lambda x: x.start)

        for i in range(len(sorted_meets) - 1):
            if sorted_meets[i].end <= sorted_meets[i+1].start:
                continue
            else:
                return False
        return True            