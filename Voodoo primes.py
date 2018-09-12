"""
Voodoo Primes

A Voodoo prime is a prime number whose reciprocal (in decimal) has the same number in its digits. For example, 7 is a voodoo prime because its reciprocal 1/7=0.14285714285 contains 7.

Examples:
Input: 3
Output: true (1/3=0.33333333333 contains 3)

Input: 11
Output: false (1/11=0.0909090909 doesn't contain 11)

Write a program to check if the user input is a Voodoo prime or not.

Bonus: Print all the Voodoo primes in a given range.

INSTRUCIONS:
Enter a range or a number
"""
def isprime(num):
    r=True
    for a in range(2,num):
        if num%a==0:
            r=False
    return r
def isvoodoo(num):
    out=False
    b=round((10**30)/num,0)
    if isprime(num):
        for s in range(0,30-len(str(num))):
            t=int("".join(list(str(int(b)))[s:s+len(str(num))]))
            if int(t)==int(num):
                out=True
        if out:
            l=1
        else:
            l=2
    else:
        l=3
    return l
numbers=list(input().replace(",","-").split("-"))
if len(numbers)==1:
    num=int(numbers[0])
    if isvoodoo(num)==1:
        print("Output: true, 1 /",num,"=",round(1/num,30)," contains",num)
    elif isvoodoo(num)==2:
        print("Output: false, 1 /",num,"=",round(1/num,30),"does not contain",num)
    elif isvoodoo(num)==3:
        print(num,"is not a prime number")
else:
    voodoolist=list()
    for num in range(int(numbers[0]),int(numbers[1])):
        if isvoodoo(num)==1:
            voodoolist.append(num)
    print("These are voodoo primes in the given range:",voodoolist)