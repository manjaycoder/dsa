class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset=set()
        for i in nums:
            if i in numset:
                return True
            numset.add(i)
        return False
        
