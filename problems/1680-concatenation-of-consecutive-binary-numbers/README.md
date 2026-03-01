# Concatenation of Consecutive Binary Numbers (LeetCode 1680)

- Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/?envType=daily-question&envId=2026-03-01
- Difficulty: Medium

## Description

Given an integer `n`, form a binary string by concatenating the binary representations of all integers from `1` to `n` in order. Return its decimal value modulo `10^9 + 7`.

## Attempt details

### Attempt 1
- Date: 2026-03-01
- Started: 10:23 PM
- Solved: 10:27 PM
- Total Time: 4 minutes

Approach: Build one large binary string by appending each integer in binary form, then convert to decimal and apply modulo.

Time Complexity: O(total bits from 1..n)
Space Complexity: O(total bits from 1..n)

To improve: Avoid constructing the full string; use iterative modulo accumulation with bit shifts for better efficiency.