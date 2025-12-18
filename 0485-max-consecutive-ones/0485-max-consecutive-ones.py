class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current=0
        best_streak=0
        for i in range(len(nums)):
            if nums[i]==1:
                current=current+1
                best_streak=max(current,best_streak)
            else:
                current=0
        return best_streak
