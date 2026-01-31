# Find Smallest Letter Greater Than Target (LeetCode 744)

- Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target
- Difficulty: Easy

## Description

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters. Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

## Attempt details

### Attempt 1
- Date: 2026-01-31
- Started: 7:56 PM
- Solved: 7:57 PM
- Total Time: 1 minute

Approach: Simple linear scan through the sorted array. Since letters are already sorted, iterate through and return the first character greater than target. If none found, return the first character (wrap around).

Time Complexity: O(n)
Space Complexity: O(1)

To improve: Could use binary search for O(log n), but linear scan is sufficient for this easy problem.
