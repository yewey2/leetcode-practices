# Find the Largest Area of Square Inside Two Rectangles (LeetCode 3047)

- Link: https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles
- Difficulty: Medium

## Description

There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.

## Attempt details

### Attempt #1
- Date: 2026-01-17
- Started: 23:15
- Solved: 23:30

We need the largest square that fits in the intersection of at least two rectangles. This adds up to checking pairwise overlaps.

Approach: Brute-force every rectangle pair, compute their intersection width and height, take the smaller side as the square size, and track the best area. This runs in O(n^2) with O(1) extra space.

To improve: Research a subquadratic method (likely sweep line or coordinate compression over edges) to skip empty overlaps when n is large.
