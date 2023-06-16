from typing import List

def numOfWays(nums: List[int]) -> int:        
    def dfs(nums: List[int]) -> int:
        if len(nums) < 3: 
            return 1
        
        left_nodes = [number for number in nums if number < nums[0]]
        right_nodes = [number for number in nums if number > nums[0]]
        return dfs(left_nodes) * dfs(right_nodes) * comb(len(nums) - 1, len(left_nodes)) % module
    
    module = pow(10, 9) + 7
    return (dfs(nums) - 1) % module