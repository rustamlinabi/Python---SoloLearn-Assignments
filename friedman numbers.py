from itertools import permutations, chain
import random, math
#[25, 121, 125, 126, 127, 128, 153, 216, 289, 343, 347, 625, 688, 736, 1022, 1024, 1206, 1255, 1260, 1285, 1296, 1395, 1435, 1503, 1530, 1792, 1827, 2048, 2187, 2349, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2508, 2509, 2592 ,2737, 2916, 3125, 3159, 3281, 3375, 3378, 3685, 3784, 3864, 3972, 4088, 4096, 4106, 4167, 4536, 4624, 4628, 5120, 5776, 5832, 6144, 6145, 6455, 6880, 7928, 8092, 8192, 9025, 9216, 9261]
#letters=str(input())
friedmannumbers=[25, 121, 125, 126, 127, 128, 153, 216, 289, 343, 347, 625, 688, 736, 1022, 1024, 1206, 1255, 1260, 1285, 1296, 1395, 1435, 1503, 1530, 1792, 1827, 2048, 2187, 2349, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2508, 2509, 2592 ,2737, 2916, 3125, 3159, 3281, 3375, 3378, 3685, 3784, 3864, 3972, 4088, 4096, 4106, 4167, 4536, 4624, 4628, 5120, 5776, 5832, 6144, 6145, 6455, 6880, 7928, 8092, 8192, 9025, 9216, 9261]
def removal(d,c):
    if len(c) > 1:
        for a in list(c):
            d.remove(a)
    else:
        d.remove(c)
def permota(x,n):
    #this one returns all the permutations of x with n numbers as a list of tuples
    d=list()
    a=list(permutations(x,n))
    for b in a:
        l=''.join((b))
        d.append(l)
    return d
def permos(a):
    #this one returns all possible permutations of [a] for every possible number of digits using permota,
    # further it is taken as a basis for [permosh()],where we take out the result of this function "out of" our
    # original number, and find all other permutations of remaining digits
    kolo=list()
    for x in range(1,len(a)):
        molo=permota(a,x)
        kolo.append(molo)
    sholo=list()
    for a in kolo:
        for b in a:
            sholo.append(b)
    return sholo
def permosh(zet,f):
    #after we calculate every possible permutation of digits in our original number, we take each permutation [f] out of
    # our original number, we find all permutations of remaining digits [zet] and using permosh we find all of
    # possible combination of permutations [f] and [zet]
    kolo=list()
    for x in range(1,len(zet)+1):
        molo=permota(zet,x)
        for zer in molo:
            deko=list()
            deko.append(zer)
            deko.append(f)
            demo = 0
            for leto in range(0, len(deko)):
                demo += len(deko[leto])
            xero=len(list(letters))-demo
            if xero==0:
                kolo.append(deko)
            else:
                ter = list(letters)[:]
                for lemo in deko:
                    removal(ter,lemo)
                re=permota(ter,xero)
                for a in re:
                    zero=deko[:]
                    zero.append(a)
                    kolo.append(zero)
                for a in ter:
                    deko.append(a)
                kolo.append(deko)
    return kolo

def comba(d,soro):
    for x in d:
        koro=list(letters)[:]
        if len(x)>1:
            for a in list(x):
                koro.remove(a)
        else:
            koro.remove(x)
        soro.append(permosh(koro,x))

def addo(a,b):
    return (a+b)
def subtracto(a,b):
    if a>b:
        return a-b
    else:
        return b-a
def multiplo(a,b):
    return a*b
def divido(a,b):
    if b==0:
        return 0
    else:
        return a/b
def exponento(a,b):
    if b>15:
        return 0
    else:
        return a**b
def expo(a,b):
    if a>15:
        return 0
    else:
        return b**a
def operpermutations(n):
    terra=list()
    perra=n*oper
    ada=list(permutations(perra,n))
    for operlist in ada:
        if operlist not in terra:
            terra.append(operlist)
        else:
            continue
    return terra
def koor(b, a):
    z = int(b[0])
    for alo in range(0, len(b) - 1):
        z = a[alo](z, int(b[alo + 1]))
    return z
operl=[addo,subtracto,multiplo,divido,exponento,expo]
def shuflo(a):
    t=list()
    while True:
        x=a[:]
        random.shuffle(x)
        if x not in t:
            t.append(x)
        else:
            continue
        if len(x)-len(set(x))==0:
            checkno=0
        else:
            checkno=len(x)-len(set(x))
        if len(t)==math.factorial(len(x)-checkno):
            break
    return t
num_of_f_nums=0
for letter in friedmannumbers:
    letters=str(letter)
    d=permos(letters)
    soro=list()
    checkn=0
    comba(d,soro)
    dero=list(chain.from_iterable(soro))
    deronew=list()
    for a in dero:
        if a not in deronew:
            deronew.append(a)
        else:
            continue
        aro=shuflo(a)
        for x in aro:
            deronew.append(x)
    oper=[addo,subtracto,multiplo,divido,exponento,expo]
    for combination in deronew:
        opercombs=operpermutations(len(combination)-1)
        for opervariation in opercombs:
            result=koor(combination,opervariation)
            if int(result)==int(letters):
                print("======================")
                print(letters,"is Friedman number")
                print("======================")
                checkn=1
                num_of_f_nums+=1
                break
            else:
                continue
        if checkn==1:
            break
        else:
            continue
    if checkn==0:
        print(letters,"NO")