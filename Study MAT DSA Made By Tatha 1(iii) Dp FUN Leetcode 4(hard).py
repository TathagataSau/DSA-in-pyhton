# -*- Leet code:4(Hard) median of twosorted arrays -*-
"""
Created on Sat Aug 13 15:13:33 2022

@author: Tathagata Sau
"""
'''
******************
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
******************

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
'''
# as It is gonna take O(log(n)) So we can understad that it kinda need Binary search.
# merging tewo arrays will be O(n+m) no log is coming. and complexity is higher at the merging prcess:
    #1. so wee need to compute a binary search on the array and getting the half of the array value,
    #2. then we can compute the nxt array Half of total lengt value - half of the prev array value.
    #3. we need to ee if the nums 1 last elemt <= the first elemt of the nums2 and vice versa. 
    #4. now the first elemt of the second pard of the each array wil be our elemt to div //2 to pic the ans.
# if we fail the 3rd condition the right shift the value by one of the prev arry
# See the other test cases in the Neetcode video


###### Solution using Binary Search:
nums1 = [1,2]
nums2 = [3,4]
A, B = nums1, nums2
total = len(nums1)+len(nums2)
half_len=(len(nums1) + len(nums2))//2
if len(B) < len(A):
    A, B = B, A
left, right = 0, len(A) - 1
while True:
    i = (left + right)//2      # for A
    j = (half_len-i-2)         #for B i and j are indexes we need so i starts at 0 and j starts at 0 so -1-1=-2
    Aleft = A[i]  if i>=0 else float("-inf")
    Aright = A[i+1] if (i+1)< len(A) else float("inf")
    Bleft = B[j]  if j>=0 else float("-inf")
    Bright = B[j+1] if (j+1)< len(B) else float("inf")
    
    # Partition is correct
    if Aleft <= Bright and Bleft <= Aright:
        # ODD
        if total % 2:
            print(min(Aright,Bright))
        # EVEN
        print((max(Aleft,Bleft) + min(Aright,Bright)) / 2)
    elif Aleft > Bright:
        right = i - 1
    else:
        left = i + 1

### Easiest Solution i've thought ♥♥♥♥♥♥♥
'''


*****************
nums=nums1+nums2
            nums3=sorted(nums)
            n=len(nums3)
            if n%2==0:
                median=(nums3[n//2-1]+nums3[n//2])/2
            else:
                
                median=nums3[n//2]
            return median
        
*******************

'''







