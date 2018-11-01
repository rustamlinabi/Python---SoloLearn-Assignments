#Transforms input text using Caesar cipher method


alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpu=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text=input()
letters=list()
for x in range(0,int(len(text))):
    letters.append(text[x:x+1])
caesar=list()
for a in letters:
    if a in alp:
        caesar.append(alp[alp.index(a)+1])
    elif a in alpu:
        caesar.append(alpu[alpu.index(a)+1])
    else:
        caesar.append(a)
unicaesar="".join(caesar)
print(unicaesar)