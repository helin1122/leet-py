
from problems.two_sums import TwoSum

def test_two_sum():
    solver = TwoSum()
    
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    assert solver.twoSum(nums, target) == [0, 1]
    
    # Test case 2
    nums = [3, 2, 4]
    target = 6
    assert solver.twoSum(nums, target) == [1, 2]
    
    # Test case 3
    nums = [3, 3]
    target = 6
    assert solver.twoSum(nums, target) == [0, 1]
    
    # Test case 4
    nums = [1, 2, 3, 4, 5]
    target = 8
    assert solver.twoSum(nums, target) == [2, 4]
    
    # Test case 5
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert solver.twoSum(nums, target) == [2, 4]