"""
Leetcode Problem: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
Category: Two Pointers (Same Direction)

Prompt:
Given an integer array `nums` sorted in non-decreasing order, 
remove the duplicates **in-place** such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it must be done in-place, do not allocate extra space for another array.
Instead, modify the input array directly and return the number of unique elements.

Constraints:
- 1 <= len(nums) <= 10⁵
- -100 <= nums[i] <= 100
- `nums` is sorted in non-decreasing order.

Return:
- An integer `k`, where the first `k` elements of `nums` contain the unique elements.
- It doesn't matter what values are left beyond the first `k`.

Example:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
# The first 5 elements should be: [0,1,2,3,4]
# You do not need to return the modified array, but it will be checked.

Tips:
- Use two pointers: one for tracking the current unique index, 
  the other to scan through the array.
- You are allowed to overwrite values in `nums`.

Do not use extra memory.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        slow = 0
        for fast in range(1,len(nums)):
            if nums[slow] != nums[fast]:
                slow +=1
                nums[slow] = nums[fast]
        
        return slow + 1