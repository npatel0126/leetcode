class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            x = target - nums[i]
            
            if x in map and map[x] != i:
                return [i, map[x]]
