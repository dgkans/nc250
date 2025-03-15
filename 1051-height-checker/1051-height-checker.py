class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy=sorted(heights)
        count=0
        for a,b in zip(heights,copy):
            if a!=b:
                count+=1
        return count