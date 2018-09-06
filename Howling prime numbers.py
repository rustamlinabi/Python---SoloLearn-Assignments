"""
Howling Primes
A howling prime is a prime number if the sum of its digits is also a prime number.

For Example:
Input:113
Output: true (113 is a prime number, 1+1+3=5 is also a prime number)
Input: 89
Output: true (89 is a prime number, 8+9=17 is also a prime number)
Input: 19
Output: false (19 is a prime number, but 1+9=10 is not a prime number)
Write a program to check if the user input is a howling prime or not.

BONUS: Print all the howling prime numbers in a given range.
"""
def isprime(num):
    r=True
    for a in range(2,10):
        if num%a==0:
            r=False
    return r
def ishowlprime(number):
    a=True
    if isprime(number):
        if number==1:
            a=" is not a prime number"
        elif isprime(number%10+int((number-number%10)/10)):
            a=" is a howling prime number"
        else:
            a=" is a prime number, but not a howling prime number"
    else:
        a=" is not a prime number"
    return str(number)+a
rango=list(input().strip("()").replace(" ",",").replace("-",",").split(","))
if len(rango)==1:
    print(ishowlprime(int(rango[0])))
else:
    listof=list()
    for a in range(int(rango[0]),int(rango[1])):
        if ishowlprime(a)==str(a)+" is a howling prime number":
            listof.append(a)
    print("This is a list of howling prime numbers in the given range",listof)