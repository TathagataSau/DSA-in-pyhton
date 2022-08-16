# -*- complexity chnge of the same problem(binary tree) -*-
"""
Created on Wed Aug 10 03:07:42 2022

@author: Tathagata Sau
"""
#first we sort then we take one card out from the middle if the numbr is greater, then the right sided all cards are eliminated and if lesser then vise versa.
#so We do a Binary Search, make the half of it then compare, again do the same
# decreasing order
cards=[8,8,6,6,6,6,6,3,2,2,2,0,0,0]
query=6
import jovian
from jovian.pythondsa import evaluate_test_cases
def locate_card(cards,query):
    lo, hi =0,len(cards)-1
    
    while lo < hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]
        print("lo:", lo,"\nhi:", hi, "\nmid:", mid,"\nmid number",mid_number)
        
        if mid_number == query and mid_number-1!= query:
            return mid
        elif mid_number<query:
            hi = mid-1
        elif mid_number>query:
            lo =mid +1
        else:
            hi = mid-1
    return -1
# for the 10^8 like large test case the the linear and the binery serach will show its effect correctly. where binery search wins by 55,000 times the linear.
#o(n) and o(log n) is different boss
