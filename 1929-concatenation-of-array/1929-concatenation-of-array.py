class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2=[]
        for i in range(len(nums)):
            nums[i]=nums2.append(nums[i])
        return nums2+nums2