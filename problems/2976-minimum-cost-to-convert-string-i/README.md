# Minimum Cost to Convert String I (LeetCode 2976)

- Link: https://leetcode.com/problems/minimum-cost-to-convert-string-i
- Difficulty: Medium

## Description

You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i]. You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y. Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

## Attempt details

### Attempt 1
- Date: 2026-02-01
- Started: 7:36 PM
- Solved: 7:52 PM
- Total Time: 16 minutes

Approach: Model character conversions as a graph of 26 lowercase letters. Initialize a 26x26 cost matrix with a large value, set direct conversion costs from input, then run Floyd-Warshall to compute all-pairs minimum conversion costs. Sum the conversion cost for each corresponding character in source and target; if any conversion is unreachable, return -1.

Time Complexity: O(26^3 + n) = O(n)
Space Complexity: O(26^2) = O(1)

To improve: None noted.
