#This code solves linear equations
#Can have variables on both sides of the equation
#Can have variables different than "x"

x=input()
b=x.split("=")
tr=list()
for n in range(0,2):
    if b[n].startswith("-"):
        tr.append(b[n])
    else:
        s='+'+b[n]
        tr.append(s)
kr=tr[1].replace('-','$').replace('+','-').replace("$","+")
tr.remove(tr[1])
tr.append(kr)
varlist=list()
nomlist=list()
for z in tr:
    c=z.replace("+","*+").replace("-","*-").split("*")
    for l in c:
        nomlist.append(l)
        for t in l:
            if t=="x":
                varlist.append(l)

for v in varlist:
    if v in nomlist:
        nomlist.remove(v)
sumnom=0
for el in nomlist:
    if el=="":
        pass
    else:
        sumnom-=int(el)
elsum=0
for ind in varlist:
    elsum+=int(ind[:-1])
print(x)
print(varlist[0][-1:],"=",sumnom/elsum)