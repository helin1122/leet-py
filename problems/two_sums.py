from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        
        Args:
            nums (List[int]): Array of integers
            target (int): Target sum value
            
        Returns:
            List[int]: Indices of the two numbers that add up to target
        """
        res: list = []
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                res = [num_map[complement], i]
                break
            num_map[num] = i
        return res
        