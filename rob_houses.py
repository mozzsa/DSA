import unittest
def rob_with_path(houses: list[int]) -> tuple[int, list[int]]:
    '''
    Rob houses with the constraint that you cannot rob two adjacent houses.
    :param houses: List of integers representing the amount of money in each house.
    :return: Tuple containing the maximum amount of money that can be robbed and the indices of the houses robbed.
    '''
    n= len(houses)
    if n==0:
        return 0,[]
    if n==1:
        return houses[0],[0]
    
    dp = [0]*n
    dp[0]=houses[0]
    dp[1]=max(houses[0],houses[1])
    
    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    # Backtrack to find the path
    path =[]
    i=n-1
    while i>=0:
        if i==0 :
            path.append(i)
            break   
        if dp[i] == dp[i-1]:
            i -= 1 # Skip this house
        else :
            path.append(i)
            i -= 2
    path.reverse()  # Reverse to get the correct order
    return dp[-1], path

#constant space solution
def rob_with_path_constant_space(houses: list[int]) -> tuple[int, list[int]]:
    '''
    Rob houses with the constraint that you cannot rob two adjacent houses using constant space. 
    :param houses: List of integers representing the amount of money in each house.
    :return: Tuple containing the maximum amount of money that can be robbed and the indices of the houses robbed.
    '''
    prev1, prev2 = 0, 0
    for value in houses:
        current = max(prev1, prev2 + value)
        prev2 = prev1
        prev1 = current

class TestRobHouses(unittest.TestCase):
    def test_rob_houses(self):
        # Test rob_with_path
        self.assertEqual(rob_with_path([]), (0, []))  # No houses
        self.assertEqual(rob_with_path([5]), (5, [0]))  # Single house
        self.assertEqual(rob_with_path([2, 7, 9, 3, 1]), (12, [1, 3]))  # Multiple houses
        self.assertEqual(rob_with_path([10, 10, 10, 10]), (20, [0, 2]))  # All houses same value
        self.assertEqual(rob_with_path([1, 2, 3, 1]), (4, [1, 3]))  # Alternating values

        # Test rob_with_path_constant_space
        self.assertEqual(rob_with_path_constant_space([]), 0)  # No houses
        self.assertEqual(rob_with_path_constant_space([5]), 5)  # Single house
        self.assertEqual(rob_with_path_constant_space([2, 7, 9, 3, 1]), 12)  # Multiple houses
        self.assertEqual(rob_with_path_constant_space([10, 10, 10, 10]),20)  # All houses same value
        self.assertEqual(rob_with_path_constant_space([1, 2, 3, 1]), 4)  # Alternating values

if __name__ == "__main__":  
    unittest.main()