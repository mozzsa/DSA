import unittest
def two_sum(nums:list, target:int)-> list:
    """
    Find two numbers in nums that add up to target.

    :param nums: List of integers.
    :param target: Target sum.
    :return: Indices of the two numbers that add up to target.
    """
    num_to_index = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    
    return []

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        self.assertEqual(two_sum([], 5), [])#no match
        self.assertEqual(two_sum([1, 2, 3], 7), [])#no match
        self.assertEqual(two_sum([1, 1, 2], 1), [0, 2])
    

if __name__ == "__main__":  
    unittest.main()
