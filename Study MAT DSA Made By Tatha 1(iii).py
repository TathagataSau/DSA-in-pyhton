# -*- generic Binery tree -*-
"""
Created on Fri Aug 12 00:44:14 2022

@author: Tathagata Sau
"""
#1. Come up with a condition to determine whether the answer lies before or after a given position
#2. Retrieve the midpoint and the middle element of the list
#3. If it is the answer. return themiddle position as the answer.
#4. if the answer lies before it, then repreat the search with the first half of the list
#5. if the answer lies after it, then repeat the seach with the second half of the list

def binary_search(lo,hi, condition):
    """ TODO- ADD docs"""
    while lo<=hi:
        mid=(lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result== 'left':
            hi = mid-1
        else:
            lo=mid+1
    return -1

## funtion in funtion is the most beautiful thing in pyhon

def locate_card(cards, query):
    
    def condition(mid):
        if cards[mid]== query:
            if mid > 0 and cards[mid-1]==query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return'left'
        else:
            return'right'
    return binary_search(0,len(cards)-1,condition)


'''
#question:
    in a sorted list print the first and the last index of the repeating number.
    
'''
# two or three test cases will be there like 
#1. the mid element is the first an last both coz' its the only one number
#2. the mid element would be the last index( i.e lest binary search for the starting number),and the mid element would be the fist element(i.e the right traversing of the binary search will take place)             