#this code checks if the user input number is "anti-Lychrel" (non-Lychrel) or not and how many iterations it takes for it to reach a palindrome.
def reverseof(x):
    d=list()
    for a in str(x):
        d.append(a)
    b=d[::-1]
    s=[""]
    for a in b:
        s[0]=s[0]+a
    return int(s[0])
def check_lyc(x):
    f=x
    fol=3
    for a in range(1,30):
        d=f+reverseof(f)
        if d==reverseof(d):
            print("Yes, it is an anti-Lychrel number, it took", a, "iteration(s) to reach a palindrome")
            fol=4
            break
        else:
            f=d
    if fol==3:
        print("No it is not an anti-Lychrel number, it did not reach a palindrome in 30 iterations")
try:
    x=int(input())
except:
    print("error, please input a number")
check_lyc(x)
