class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1,len(nums)):
                if temp == nums[j]:
                    count +=1
                else:
                    continue
        return count
