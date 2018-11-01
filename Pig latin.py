#English to Pig latin translator

con=['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'b', 'v', 'c', 'x', 'z', 'Q', 'W', 'R', 'T', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

tex=input().lower()
let=list()
for z in range(0,len(tex)):
    let.append(tex[z:z+1])
if let[0] in con:
    n=0
    for t in range(0,len(tex)):
        if let[t] in con:
            n=t+1
        else:
            break
    pig=let[n:]
    for t in let[:n]:
        pig.append(t)
    pig.append('ay')
    pigl="".join(pig)
else:
    pigl=tex+'yay'
print(pigl.capitalize())