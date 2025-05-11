class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h_aug = [(heights[i],i) for i in range(len(heights))]

        h_aug.sort(key=lambda item:item)
        res = 0
        for i in range(len(h_aug)):
            ele, idx = h_aug[i]
            if idx!=i and ele!=heights[i]:
                res += 1
        
        return res