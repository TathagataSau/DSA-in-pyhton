# -*- Leetcode 70:stair case -*-
"""
Created on Sat Aug 13 14:18:04 2022

@author: Tathagata Sau
"""
''''
Leet code 70: climbing stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
*************************************    
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
example 2:
    ***********************************************
    Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

If forget the complexity steps see the NeetCode Video Climbing stairs.
'''
#step 1: describe the problem
#step 2: can be solved using, Bruteforce, Tree, DFS, DP
#step 3: explain all the complexities of all the problems
#step 4: choose the best one, then choose the one has better space complexity also or manupulate the list. 
#solution
n=8              #will be in the class solution
prev, nxt = 1, 1
for i in range(n-1):
    temp = prev
    prev = prev + nxt
    nxt = temp
print(prev)
    