# Divide an Array Into Subarrays With Minimum Cost I (LeetCode 3010)

- Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/?envType=daily-question&envId=2026-01-31
- Difficulty: Easy

## Description

You are given an array of integers nums of length n. The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3. You need to divide nums into 3 disjoint contiguous subarrays. Return the minimum possible sum of the cost of these subarrays.

## Attempt details

### Attempt 1
- Date: 2026-02-01
- Started: 7:32 PM
- Solved: 7:34 PM
- Total Time: 2 minutes

Approach: The first subarray must start at index 0 (since it's contiguous), so nums[0] is always included in the cost. For the remaining two subarrays, we need to minimize their starting elements. Sort nums[1:] and take the two smallest values.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for the sorted slice

To improve: None needed - clean and efficient solution for this easy problem.
