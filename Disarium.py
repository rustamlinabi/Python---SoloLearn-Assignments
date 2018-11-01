"""
A number is called a Disarium number if the sum of the powers of its digits equals the number itself, where the digits are powered to their position in the number. This code finds Disarium numbers in a range or defines if given number is a disarium number
"""
a=input().replace(" ","-").replace(",","-").split("-")
def dis(a):
    b=list(str(a))
    t=0
    for r in range(1,len(b)+1):
        t+=int(b[r-1])**r
    l=True if t==a else False
    return l
if len(a)==1:
    if dis(int(a)):
        print(a,"is a disarium number")
else:
    dislist=list()
    for l in range(int(a[0]),int(a[1])):
        if dis(l):
            dislist.append(l)
    print("Disarium numbers in given range are",dislist)