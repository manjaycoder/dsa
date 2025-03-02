class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in nums_map:
                return [nums_map[complement],i]
            nums_map[num]=i
        

        
        
        
        