class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result=[]
        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num)
        return result

        