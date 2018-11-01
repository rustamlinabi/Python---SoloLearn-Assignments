"""
A number is called a Disarium number if the sum of the powers of its digits equals the number itself, where the digits are powered to their position in the number. This code finds Disarium numbers in a range or defines if given number is a disarium number
"""
(lambda b:(lambda a: print (b,"is a disarium number") if sum([(t[1]**(t[0]+1)) for t in list(enumerate([int(num) for num in a]))])==b else print(b,"is not a disarium number"))(a=list(str(b))))(b=int(input()))