"""
Guitar Subset

For a list of integers S and a target number G, a subset of S that adds up to G is called a guitar subset.

For example:
Input:
24
[12, 1, 61, 5, 9, 2]
Output:
[12, 9, 2, 1]
(G=24, S=[12, 1, 61, 5, 9, 2], there is a guitar subset [12, 9, 2, 1] that adds up to 24).

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

Write a program to check if the user input has a guitar subset for the specified number G or not (both the list of integers and the number G are input parameters).
"""
import random, math
from itertools import permutations
print("Enter G number in the first line and S subset in the second line")
g=int(input())
s=list(map(int,input().replace(" ",",").replace(";",",").split(",")))
def guitarsubset(g,s):
    x=False
    for a in range(1,len(s)):
        perm=list(permutations(s,a))
        for b in perm:
            if sum(b)==g:
                print("For G",g,"and S",s,"guitar subset is",list(b))
                x=True
                break
        if x:
            break
    if x==False:
        print("There is no guitar subset for given G:",g," and S:", s)
guitarsubset(g,s)