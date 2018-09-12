"""
Strange Root

A number has a strange root if its square and square root share any digit. For example, 2 has a strange root because the square root of 2 equals 1.414 and it contains 4 (which is the square of 2).

Examples:
Input: 11
Output: true
(the square root of 11 is 3.317, the square of 11 is 121. They share the same digit (1).)

Input: 24
Output: false (the square root of 24 (4.899) and square (576) do not share any digits)

Write a program to check if the user input has a strange root or not.
"""
a=int(input())
print(a,"does not have a strange root") if len(set(list(str(round(a**0.5,3)))))+len(set(list(str(a**2))))==len(set(list(str(round(a**0.5,3)))+list(str(a**2)))) else print(a,"has a strange root, sharing following numbers:",set(str(round(a**0.5,3)))&set(str(a**2)))