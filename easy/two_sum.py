# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time
# complexity?

################################################################################

def two_sum(nums: list[int], target: int, current_index: int,
            additional_index: int) -> list[int]:
    if current_index < (len(nums) - 1):
        current_element = nums[current_index]

        for idx, number in enumerate(nums):
            if idx != current_index:
                if (current_element + number) == target:
                    additional_index = idx
                    return current_index, additional_index

    return two_sum(nums, target, current_index + 1, additional_index)


# Testes
# Example 1:
nums = [2, 7, 11, 15]
target = 9

# Example 2:
# nums = [3, 2, 4]
# target = 6

# Example 3:
# nums = [3, 3]
# target = 6

print(two_sum(nums, target, 0, 0))

# Resultado para a proposta apresentada:
# - 57 / 57 test cases passed.
# - Runtime: 7456 ms
# - Memory Usage: 25.4 MB
