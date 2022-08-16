# -*- Binary Search, Linked lists and complexity -*-
"""
Created on Tue Aug  9 15:56:28 2022

@author: Tathagata Sau
"""
# a Number of card is given AND i have to locate the no. 7 card with Binary search
'''
1.State the problem clearly. Identify the Inputs and output formats
2.Come up  with some example input and outputs, including edge cases.
3.come up with the correct solution  of the problem.State it in plane english.
4.Implement the solution and tet it Using Examples, Fix bugs If any.
5.Analyze the algorithm's complexity and Identify inefficiencies, if any.
6.Apply the right technique to overcome the inefficiency. Repeat Steps 3 and 6.

"Applying the right technique" is where the knowledgeof common DSA in Handy. 
'''
# either speak ou t loud to the interviewer or write it down in your own language.
#1.We need to write a program to find the position of a given nnumber is a ist of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from  the given list.
#2.say input cards= [13,11,12,7,4,3,1,0]sorted list
#3.query: A number whose position in the list to be determined E.g 7
#4.position: The position of the query in the list cards. Eg. # in the above case(counting from 0)

test = {
        'input':{
            'cards':[13,11,12,7,4,3,1,0],
            'query':7
            },
        'output':3
        }
"""
def locate_card(cards,query):    #name the func carefully coz' the code may be shared with the company, also the variables should be named properly
    pass                         #atleat someting you need to write and pass doesn't do anything so its ok.
 """   
#locate_card(**test['input'])==test['output']    #** takes the takes keys and values as arguements from the dictionary
# think the test cases
#0.somehwere middle in the list(general/avg case)
#1.first elem
#2.last elem
#3.the list contain only one number which is query
#4.the list doesn't contain number query
#5.the list card is empty
#6.the list card contains repeating numbers.
#7.the number query occurs at more than one position in cards

tests=[]
tests.append(test)

tests.append({
    'input':{
    'cards':[13,11,12,7,4,3,1,0],
    'query':1
    },
'output':6
})

tests.append({
    'input':{
    'cards':[4,2,1,-1],
    'query':4
    },
'output':0
})
tests.append({
    'input':{
    'cards':[3,-1,-9,-127],
    'query':-127
    },
'output':3
})

tests.append({
    'input':{
    'cards':[6],
    'query':6
    },
'output':0
})

tests.append({
    'input':{
    'cards':[13,11,12,7,4,3,1,0],
    'query':1
    },
'output':6
})      
# if doesn't exists return -1
tests.append({
    'input':{
    'cards':[9,7,5,2,-9],
    'query':4
    },
'output':-1
})

tests.append({
    'input':{
    'cards':[],
    'query':7
    },
'output':-1
})

tests.append({
    'input':{
    'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],
    'query':3
    },
'output':7
})

tests.append({
    'input':{
    'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],
    'query':6
    },
'output':2
})

#done it all the test cases

#the solution in simple english
# Brute Force Solution
'''
1.create a variables with value 0
2.check if the number at the index position in card equals query.
3. if does, the potion is the ans, and can be returned from func.
4.if not, increment the value of the position by 1, and repeat the steps 2 & 5 till we reach the last position.
5. If thenumber was not found, return -1.
'''
# linear search
"""
def locate_card(cards,query):
    position = 0
    while True:
        if cards[position]==query:
            return position
        position+=1
        if position ==len(cards):
            return -1
"""
#rewrite the func
'''
def locate_card(cards,query):
    position = 0
    print('cards:',cards)
    print('query:',query)
    while True:
        print('position:',position)
        
        if cards[position]==query:
            return position
        position+=1
        if position ==len(cards):
            return -1
'''
#re-write after understanding the error in 6th test case
def locate_card(cards,query):
    position = 0
    while position<len(cards):
        if cards[position]==query:
            return position
        position+=1
        
    return -1 
      
result = locate_card(test['input']['cards'],test['input']['query'])
print(str(result)+" True")

from jovian.pythondsa import evaluate_test_case
evaluate_test_case(locate_card, test)

from jovian.pythondsa import evaluate_test_cases
for test in tests:
    print(locate_card(**test['input'])==test['output'])

evaluate_test_case(locate_card, tests)
#write the indexes so that we can acess the situation
'''
cards6 = tests[6]['input']['cards']
query6 = tests[6]['input']['query']
'''
# write in terminal to check
'''
tests[6]
locate_card(cards6, query6) 
'''
## now we got to know that we are trying to access the 0th position of the empty list LOL

# till now its an avg case





