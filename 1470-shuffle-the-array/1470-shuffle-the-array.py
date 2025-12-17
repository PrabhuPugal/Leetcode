class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #nums2=[]
        #i=0
        #j=n
        #for k in range(n):
        #    nums2.append(nums[i])
         #   nums2.append(nums[j])
          #  i+=1
           # j+=1
        #or you could also do this
        res = []
        for i in range(n):
            res+=[nums[i]]
            res+=[nums[i+n]]
        return res

