# -*- Leetcode 48:image rotation -*-
"""
Created on Sat Aug 13 14:32:49 2022

@author: Tathagata Sau
"""

'''
**********************
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
**********************


Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
# remeber Computer can not compute more than 10^8 values at a time
# solution: visualise the thing, i'll draw at the time of study
matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix[0])
for row in range(n):
    for col in range(row,n):
        matrix[col][row],matrix[row][col]=matrix[row][col],matrix[col][row]
# i part of the matix = matrix[col][row] = matrix[row][col]
# j part of the matix = matrix[row][col] = matrix[col][row]
# now i've done transposing this matrix
# now i'll have to revese each row of the matrix
    matrix[row].reverse()
print(matrix)
