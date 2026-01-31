# Find Closest Person (LeetCode 3516)

- Link: https://leetcode.com/problems/find-closest-person
- Difficulty: Easy

## Description

You are given three integers x, y, and z, representing the positions of three people on a number line. Both Person 1 and Person 2 move toward Person 3 at the same speed. Determine which person reaches Person 3 first. Return 1 if Person 1 arrives first, 2 if Person 2 arrives first, or 0 if both arrive at the same time.

## Attempt details

### Attempt 1
- Date: 2026-01-31
- Started: 7:58 PM
- Solved: 7:59 PM
- Total Time: 1 minute

Approach: Calculate the absolute distance from each person to Person 3. Compare distances: if d1 < d2 return 1, if d2 < d1 return 2, otherwise return 0.

Time Complexity: O(1)
Space Complexity: O(1)

To improve: None needed - straightforward implementation for this easy problem.
