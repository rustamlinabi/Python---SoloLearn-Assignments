#This code presents very large or small numbers in a more readable way.

a=float(input().replace(",","."))

for d in range (-30,30):
   t=a*(10**d)
   l=-d
   if t>1 and t<10:
       break
print(t,"* 10 ^",l)