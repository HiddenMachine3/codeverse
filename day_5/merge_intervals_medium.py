class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item:(item[0], item[1]))

        to_include = [False for _ in intervals]
        to_include[0] = True
        curr_item = 0
        i = 1
        while i<len(intervals):

            start, end = intervals[i]
            if start <= intervals[curr_item][1]:
                intervals[curr_item][1] = max(intervals[curr_item][1], end)
            else:
                curr_item = i
                to_include[i] = True
            i += 1
        merged = [intervals[i] for i in range(len(intervals)) if to_include[i]]
        return merged