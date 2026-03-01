# Partitioning Into Minimum Number Of Deci-Binary Numbers (LeetCode 1689)

- Link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/
- Difficulty: Medium

## Description

Given a positive decimal string `n`, return the minimum number of positive deci-binary numbers (digits only 0 or 1) whose sum equals `n`.

## Attempt details

### Attempt 1
- Date: 2026-03-01
- Started: 10:19 PM
- Solved: 10:20 PM
- Total Time: 1 minute

Approach: The minimum count is the maximum digit in `n`, because each deci-binary addend can contribute at most `1` to each digit position.

Time Complexity: O(n)
Space Complexity: O(1)

To improve: Could simplify `max(i for i in str(n))` to `max(n)` since `n` is already a string.