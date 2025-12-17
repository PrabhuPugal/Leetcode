class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i, j in enumerate(nums):
            difference=target-j
            if difference in visited:
                return [visited[difference],i]
            visited[j]=i
        return []
                
            