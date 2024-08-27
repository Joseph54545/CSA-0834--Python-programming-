def sumsqr(n):
    l=[]
    while n>=1:
        i=int(input("enter the elements"))
        l.append(i)
        n=n-1
        even=0
        odd=0
    for p in l:
        if p%2==0:
            even=even+p**2
        else:
            odd=odd+p**2
    k=[odd,even]
    return k
n=int(input("enter a numberofelements"))
print (sumsqr(n))
