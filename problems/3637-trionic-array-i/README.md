# Trionic Array I (LeetCode 3637)

- Link: https://leetcode.com/problems/trionic-array-i/
- Difficulty: Easy

## Description

You are given an integer array nums of length n. An array is trionic if there exist indices 0 < p < q < n − 1 such that:

- nums[0...p] is strictly increasing,
- nums[p...q] is strictly decreasing,
- nums[q...n − 1] is strictly increasing.

Return true if nums is trionic, otherwise return false.

## Attempt details

### Attempt 1
- Date: 2026-02-03
- Started: 9:54 AM
- Stopped: 9:59 AM (first attempt)
- Continued: 2:40 PM
- Solved: 2:47 PM
- Total Time: 12 minutes

Approach: Track direction changes while scanning the array and count transitions from increasing to decreasing to increasing. Reject if any equal elements or too many transitions. Ensure the array starts with an increase and ends with an increase for valid trionic pattern.

Time Complexity: O(n)
Space Complexity: O(1)

To improve: Remove debug prints and tighten the transition logic for clarity.
