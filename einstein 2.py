"""
Einstein's Riddle

Einstein's Riddle is a logic puzzle. It is often claimed that only 2% of the population can solve the puzzle.

It has several variants, one of them is this:
1. There are five houses.
2. The Mathematician lives in the red house.
3. The Hacker writes in Python.
4. Brackets (code editor) is used in the green house.
5. The Analyst uses Atom (code editor).
---6. The green house is immediately to the right of the ivory house.
7. The man who uses Redis (Database System) writes in Java.
8. Cassandra (Database System) is used in the yellow house.
9. Notepad++ (code editor) is used in the middle house.
10. The Developer lives in the first house.
---11. The man who uses Hadoop (Database System) lives in the house next to the man writing in JavaScript.
---12. Cassandra is used in the house next to the house where the primary language is C#.
13. The man who uses ArangoDB uses Sublime Text (code editor).
14. The Engineer uses MongoDB.
---15. The Developer lives next to the blue house.

Now, who uses Vim? Who writes in C++?

Write a program that solves this riddle and outputs the answer.
"""
import itertools
profs = ["Math", "Hacker", "Analyst", "Developer", "Engineer"]
langs = ["python", "java", "c", "javascript", "c++"]
houses = ["red", "green", "ivory", "blue", "yellow"]
edits = ["atom", "brackets", "notepad", "sublime", "vim"]
datab = ["redis", "cassandra", "hadoop", "arango", "mongo"]
order = [1, 2, 3, 4,5]
alllist = list()
#This will give us all possible house combinations
for a in range(0, 5):
    for b in range(0, 5):
        for c in range(0, 5):
            for d in range(0, 5):
                for e in range(0, 5):
                    for f in range(0, 5):
                        reylo = [profs[a], langs[b], houses[c], edits[d], datab[e], order[f]]
                        alllist.append(reylo)
colist = alllist[:]
#I divided all arguments into two, the first kind of arguments are "first order" conditions, i.e. those which are
#do not entail more than one house,namely 2,3,4,5,7,8,9,10,13,14. The second kind of arguments are "second order",
#6,11,12,15. We will deal with those further below
for a in alllist:
    if (a[0] == "Math") != (a[2] == "red") or (a[0] == "Hacker")!= (a[1] == "python") or (a[3]=="brackets")!=(a[2]=="green") or (a[3] == "atom") != (a[0]=="Analyst") or (a[4]=="redis")!=(a[1]=="java") or (a[4]=="cassandra")!=(a[2]=="yellow") or (a[3]=="notepad")!=(a[5]==3) or (a[0]=="Developer")!=(a[5]==1) or (a[4]=="arango")!=(a[3]=="sublime") or (a[0]=="Engineer")!=(a[4]=="mongo") or (a[2]=="blue")!=(a[5]==2):
        try:
            colist.remove(a)
        except:
            continue
cocolist=colist[:]
#here I decided to divide all remaining houses based on their owner
mathlist=list()
devellist=list()
hackerlist=list()
engineerlist=list()
analist=list()
for a in cocolist:
    if a[0]=="Math":
        mathlist.append(a)
for a in cocolist:
    if a[0]=="Hacker":
        hackerlist.append(a)
for a in cocolist:
    if a[0]=="Developer":
        devellist.append(a)
for a in cocolist:
    if a[0]=="Engineer":
        engineerlist.append(a)
for a in cocolist:
    if a[0]=="Analyst":
        analist.append(a)
#This gives us combinations of all "neighborhoods"
comblist=list()
for a in mathlist:
    for b in hackerlist:
        for c in devellist:
            for d in engineerlist:
                for e in analist:
                    treno=[a,b,c,d,e]
                    if len(list(itertools.chain.from_iterable(treno)))==len(set(itertools.chain.from_iterable(treno))):
                        comblist.append(treno)
fincomblist=comblist[:]
#Finally,here we check for "second order" conditions
for a in comblist:
    for b in range(0,5):
        if a[b][2] == "green":
            for c in range (0,5):
                if a[c][2]=="ivory":
                    if a[b][5]-a[c][5]!=1:
                        try:
                            fincomblist.remove(a)
                        except:
                            continue
        if a[b][4]=="hadoop":
            for c in range(0,5):
                if a[c][1]=="javascript":
                    if a[b][5]-a[c][5]==1:
                        continue
                    elif a[b][5]-a[c][5]==-1:
                        continue
                    else:
                        try:
                            fincomblist.remove(a)
                        except:
                            continue
        if a[b][4]=="cassandra":
            for c in range(0,5):
                if a[c][1]=="c":
                    if a[b][5]-a[c][5]==1:
                        continue
                    elif a[b][5]-a[c][5]==-1:
                        continue
                    else:
                        try:
                            fincomblist.remove(a)
                        except:
                            continue
solution=fincomblist[0]
print("Solution is as following:")
for a in solution:
    if a[3]=="vim":
        print("Vim is used by",a[0],"in the house number",a[5])
    if a[1]=="c++":
        print(a[0],"in the house number", a[5],"writes in c++")
for d in range(1,6):
    for a in solution:
        if a[5]==d:
            print("The house number",d,"is",a[0:5])